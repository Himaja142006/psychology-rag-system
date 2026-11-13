import fitz

# Step 1: Specify the PDF file path
pdf_path = "documents/psychology.pdf"

# Step 2: Open the PDF document
document = fitz.open(pdf_path)

# Step 3: Create an empty string to store extracted text
extracted_text = ""

# Step 4: Extract text from every page
for page_number, page in enumerate(document, start=1):

    text = page.get_text()

    extracted_text += f"\n\n--- Page {page_number} ---\n\n"
    extracted_text += text

# Step 5: Save the extracted text
output_path = "data/extracted_text.txt"

with open(output_path, "w", encoding="utf-8") as file:
    file.write(extracted_text)

# Step 6: Display extraction results
print("PDF text extraction completed successfully!")

print("Total pages:", len(document))

print("Total characters extracted:", len(extracted_text))

print("\nPreview of extracted text:\n")

print(extracted_text[:1000])

# Step 7: Close the PDF
document.close()