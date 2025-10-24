import os
import json
import nltk
from datasets import load_dataset
from transformers import (
    T5ForConditionalGeneration,
    T5Tokenizer,
    TrainingArguments,
    Trainer,
    DataCollatorForSeq2Seq
)
from peft import LoraConfig, get_peft_model, TaskType

# Disable symlink warnings
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"


MODEL_NAME = "t5-small"
INPUT_DIR = "processed_content"
OUTPUT_DIR = "t5-ncert-qg-model"
TRAIN_EPOCHS = 3
PER_DEVICE_TRAIN_BATCH_SIZE = 4
LEARNING_RATE = 5e-5


try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')
try:
    nltk.data.find('tokenizers/punkt_tab')
except LookupError:
    nltk.download('punkt_tab')
try:
    nltk.data.find('taggers/averaged_perceptron_tagger_eng')
except LookupError:
    nltk.download('averaged_perceptron_tagger_eng')
try:
    nltk.data.find('taggers/averaged_perceptron_tagger')
except LookupError:
    nltk.download('averaged_perceptron_tagger')

# Create target question
def create_target_question(sentence, label):
    if label == "Easy":
        tokens = nltk.word_tokenize(sentence)
        tagged_tokens = nltk.pos_tag(tokens)
        for i in range(len(tagged_tokens) - 1, -1, -1):
            if tagged_tokens[i][1].startswith('NN'):
                tokens[i] = "_______"
                return " ".join(tokens)
    return sentence


# Preprocess Function
def preprocess_function(examples):
    inputs, targets = [], []
    for sentence, label in zip(examples["sentence"], examples["label"]):
        if not sentence or not label or label == "Uncategorized":
            continue
        prompt = f"generate {label.lower()} question: {sentence.strip()}"
        target = create_target_question(sentence.strip(), label)
        if target.strip():
            inputs.append(prompt)
            targets.append(target)
    if not inputs:
        return {"input_ids": [], "attention_mask": [], "labels": []}
    model_inputs = tokenizer(inputs, max_length=128, truncation=True, padding="max_length")
    labels = tokenizer(targets, max_length=128, truncation=True, padding="max_length")
    model_inputs["labels"] = labels["input_ids"]
    return model_inputs


# MAIN EXECUTION
if __name__ == "__main__":
    if not os.path.exists(INPUT_DIR):
        print(f"Error: Input directory '{INPUT_DIR}' not found.")
        print("Please run 'text_processor.py' first.")
    else:
        print("Loading dataset...")
        json_files = [os.path.join(path, name) for path, subdirs, files in os.walk(INPUT_DIR)
                      for name in files if name.endswith(".json")]
        dataset = load_dataset('json', data_files=json_files, split='train')
        print(f"Dataset loaded with {len(dataset)} examples.")


        # Debug check: find problematic examples
        def inspect_dataset(dataset, limit=10):
            bad_samples = []
            for i, example in enumerate(dataset):
                try:
                    if not example.get("sentence") or not example.get("label"):
                        bad_samples.append((i, "missing_field"))
                        continue
                    if not isinstance(example["sentence"], str) or not isinstance(example["label"], str):
                        bad_samples.append((i, "non_string"))
                        continue
                    if len(example["sentence"].strip()) == 0 or len(example["label"].strip()) == 0:
                        bad_samples.append((i, "blank_text"))
                        continue
                except Exception as e:
                    bad_samples.append((i, str(e)))
                if len(bad_samples) >= limit:
                    break
            print(f"Found {len(bad_samples)} bad examples (showing up to {limit}):")
            for idx, reason in bad_samples:
                print(f"Index {idx}: {reason}")

        inspect_dataset(dataset)


        # Filter invalid rows
        def valid_example(example):
            return (example["sentence"] and example["label"]
                    and example["label"] != "Uncategorized"
                    and len(example["sentence"].strip()) > 0)
        dataset = dataset.filter(valid_example)
        print(f"Dataset after filtering: {len(dataset)} valid examples.")

        # Tokenize and preprocess
        print("Loading tokenizer and preprocessing data...")
        tokenizer = T5Tokenizer.from_pretrained(MODEL_NAME)
        tokenized_dataset = dataset.map(preprocess_function, batched=True)
        print("Data preprocessing complete.")

        # Load model and apply LoRA
        print(f"Loading base model: {MODEL_NAME}")
        model = T5ForConditionalGeneration.from_pretrained(MODEL_NAME)
        lora_config = LoraConfig(
            r=16, lora_alpha=32, target_modules=["q", "v"],
            lora_dropout=0.05, bias="none", task_type=TaskType.SEQ_2_SEQ_LM
        )
        model = get_peft_model(model, lora_config)
        model.print_trainable_parameters()

        # Training setup
        training_args = TrainingArguments(
            output_dir=OUTPUT_DIR,
            num_train_epochs=TRAIN_EPOCHS,
            learning_rate=LEARNING_RATE,
            per_device_train_batch_size=PER_DEVICE_TRAIN_BATCH_SIZE,
            weight_decay=0.01,
            logging_dir='./logs',
            logging_steps=10,
            save_total_limit=2,
        )
        data_collator = DataCollatorForSeq2Seq(tokenizer=tokenizer, model=model)

        trainer = Trainer(
            model=model,
            args=training_args,
            train_dataset=tokenized_dataset,
            data_collator=data_collator,
        )

        print("\nStarting model training...")
        trainer.train()
        print("Training complete.")

        print(f"Saving fine-tuned model to {OUTPUT_DIR}...")
        model.save_pretrained(OUTPUT_DIR)
        tokenizer.save_pretrained(OUTPUT_DIR)
        print("Model saved successfully.")
        print("this is not optimized")
        
