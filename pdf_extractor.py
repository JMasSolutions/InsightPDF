import pdfplumber

def extract_text_with_progress(file_path, progress_callback):
    """
    Extracts text from a PDF file and updates progress via a callback.

    Args:
        file_path (str): The path to the PDF file.
        progress_callback (function): A function to call with progress updates (value between 0 and 1).

    Returns:
        str: The extracted text.
    """
    extracted_text = ''
    try:
        with pdfplumber.open(file_path) as pdf:
            total_pages = len(pdf.pages)
            for i, page in enumerate(pdf.pages):
                page_text = page.extract_text()
                if page_text:
                    extracted_text += page_text + '\n'
                else:
                    print(f"No text found on page {i + 1}.")
                # Update progress via the callback
                progress = (i + 1) / total_pages
                progress_callback(progress)
        return extracted_text
    except Exception as e:
        print(f"An error occurred: {e}")
        raise e  # Re-raise exception to be handled by the caller