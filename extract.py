import pdfplumber

def extract_text_from_pdf(pdf_path):
    # This function utilizes pdfplumber to extract text from pdfs maintaining the pdf structure.
    # It returns alls the extracted text which then will be later used to index and summarize.
    text = ''
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page_number, page in enumerate(pdf.pages):
                page_text = page.extract_text()
                if page_text:
                    text += page_text + '\n'
                else:
                    print(f"No text found on page {page_number + 1}.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return text

