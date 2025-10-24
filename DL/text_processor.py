import os
import json
import re


def clean_text(text):
    text = text.replace("-\n", "")
    text = text.replace("\n", " ")
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def split_into_sentences(text):
    sentences = re.split(r'(?<=[.?!])\s+(?=[A-Z0-9])', text)
    return [s.strip() for s in sentences if s.strip()]


def apply_heuristics(sentence):
    """
    Applies simple rules to label a sentence with a difficulty level.
    """
    sentence_lower = sentence.lower()

    # Easy: Sentences that are likely definitions or simple facts.
    easy_keywords = ["is defined as", "is called", "is known as", "the s.i. unit", "consists of", "is equal to"]
    if any(keyword in sentence_lower for keyword in easy_keywords):
        return "Easy"

    # Medium: Sentences that likely explain a process, reason, or consequence.
    medium_keywords = ["because", "therefore", "as a result", "due to", "in order to", "however", "furthermore"]
    if any(keyword in sentence_lower for keyword in medium_keywords):
        return "Medium"

    # Default label if no specific keywords are found.
    return "Uncategorized"


def process_extracted_content(input_dir, output_dir):
    """
    Reads the JSON files from the extraction step, processes the text,
    and saves the labeled sentences into new JSON files.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created directory: {output_dir}")

    # Walk through the directory of extracted content
    for root, dirs, files in os.walk(input_dir):
        for filename in files:
            if filename.lower().endswith(".json"):
                json_path = os.path.join(root, filename)
                print(f"\nProcessing file: {json_path}...")

                with open(json_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)

                all_labeled_sentences = []
                for page_data in data:
                    raw_text = page_data.get("text", "")
                    page_num = page_data.get("page_number", "N/A")

                    cleaned_text = clean_text(raw_text)

                    # Skip completely blank pages
                    if not cleaned_text or len(cleaned_text.strip()) == 0:
                        continue

                    sentences = split_into_sentences(cleaned_text)

                    for sentence in sentences:
                        sentence = sentence.strip()

                        # Skip very short fragments or non-text lines
                        if len(sentence) < 5 or not any(c.isalpha() for c in sentence):
                            continue

                        label = apply_heuristics(sentence)

                        # Skip weak samples if you don't want them in training
                        if label == "Uncategorized":
                            continue

                        all_labeled_sentences.append({
                            "sentence": sentence,
                            "label": label,
                            "source_page": page_num,
                            "source_file": filename,
                        })

               # directory to save the json 
                relative_path = os.path.relpath(root, input_dir)
                output_path_dir = os.path.join(output_dir, relative_path)

                if not os.path.exists(output_path_dir):
                    os.makedirs(output_path_dir)

                if len(all_labeled_sentences) == 0:
                    print(f"Invalid sentences found in {filename}, skipping file.")
                    continue

                output_json_path = os.path.join(output_path_dir, f"processed_{filename}")
                with open(output_json_path, 'w', encoding='utf-8') as jf:
                    json.dump(all_labeled_sentences, jf, indent=4, ensure_ascii=False)

                print(f"Saved {len(all_labeled_sentences)} labeled sentences to: {output_json_path}")


if __name__ == "__main__":
    # The directory where the output of the first script was saved.
    INPUT_DIRECTORY = "extracted_content"
    # A new directory where the processed and labeled data will be saved.
    OUTPUT_DIRECTORY = "processed_content"

    if not os.path.exists(INPUT_DIRECTORY):
        print(f"Error: Input directory '{INPUT_DIRECTORY}' not found.")
        print("Please run the 'pdf_extractor.py' script first.")
    else:
        process_extracted_content(INPUT_DIRECTORY, OUTPUT_DIRECTORY)
        print("\nText processing and labeling complete.")

