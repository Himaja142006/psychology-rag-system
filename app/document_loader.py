import fitz


def extract_text_from_pdf(pdf_path):

    # Open the PDF document
    document = fitz.open(pdf_path)

    extracted_text = ""

    # Extract text from every page
    for page_number, page in enumerate(document, start=1):

        text = page.get_text()

        extracted_text += f"\n\n--- Page {page_number} ---\n\n"
        extracted_text += text

    # Close the PDF
    document.close()

    return extracted_text