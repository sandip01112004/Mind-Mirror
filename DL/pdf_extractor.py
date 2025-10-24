import fitz  # PyMuPDF
import os
import json

def extract_content_from_pdfs(pdf_dir, output_dir):
    
    # Create the main output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created directory: {output_dir}")

    # Recursively walk through the input directory
    for root, dirs, files in os.walk(pdf_dir):
        for filename in files:
            if filename.lower().endswith(".pdf"):
                pdf_path = os.path.join(root, filename)
                print(f"\nProcessing file: {pdf_path}...")

               
                relative_path = os.path.relpath(root, pdf_dir)
                base_filename = os.path.splitext(filename)[0]

           
                if relative_path == ".":
                    pdf_output_folder = os.path.join(output_dir, base_filename)
                else:
                    pdf_output_folder = os.path.join(output_dir, relative_path, base_filename)

                image_folder = os.path.join(pdf_output_folder, 'images')

                if not os.path.exists(pdf_output_folder):
                    os.makedirs(pdf_output_folder)
                if not os.path.exists(image_folder):
                    os.makedirs(image_folder)

           
                doc = fitz.open(pdf_path)
                pdf_data = [] 

                # Iterate
                for page_num, page in enumerate(doc):
                    text = page.get_text("text")

                    image_list = page.get_images(full=True)
                    image_paths = []

                    for i, img in enumerate(image_list):
                        xref = img[0]
                        try:
                            base_image = doc.extract_image(xref)
                            image_bytes = base_image["image"]
                            image_ext = base_image["ext"]

                            image_filename = f"page_{page_num + 1}_img_{i + 1}.{image_ext}"
                            image_path = os.path.join(image_folder, image_filename)

                            with open(image_path, "wb") as img_file:
                                img_file.write(image_bytes)
                            
                            image_paths.append(os.path.join('images', image_filename))

                        except Exception as e:
                            print(f"  - Warning: Could not extract image {i+1} on page {page_num+1}. Error: {e}")


                    # Append the extracted data for this page to our list
                    page_content = {
                        'page_number': page_num + 1,
                        'text': text.strip(),
                        'images': image_paths
                    }
                    pdf_data.append(page_content)

                # save in json format
                json_path = os.path.join(pdf_output_folder, f"{base_filename}.json")
                with open(json_path, 'w', encoding='utf-8') as jf:
                    json.dump(pdf_data, jf, indent=4, ensure_ascii=False)

                print(f"  - Successfully extracted {len(doc)} pages.")
                print(f"  - Saved structured text to: {json_path}")
                print(f"  - Saved images to: {image_folder}")

                doc.close()

if __name__ == "__main__":

    PDF_DIRECTORY = "NCERT"  
    OUTPUT_DIRECTORY = "extracted_content"

    # if the folder does not exist
    if not os.path.exists(PDF_DIRECTORY):
        os.makedirs(PDF_DIRECTORY)
        print(f"Created input directory: {PDF_DIRECTORY}")
        print(f"Please place your NCERT subfolders (9 and 10) in the '{PDF_DIRECTORY}' folder and run this script again.")
    else:
        extract_content_from_pdfs(PDF_DIRECTORY, OUTPUT_DIRECTORY)
        print("\nExtraction process complete.")

