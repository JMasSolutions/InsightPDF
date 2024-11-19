from tkinter import messagebox
import pdfplumber

def extract_text_with_progress(self, file_path):
    self.extracted_text = ''
    try:
        with pdfplumber.open(file_path) as pdf:
            total_pages = len(pdf.pages)
            for i, page in enumerate(pdf.pages):
                page_text = page.extract_text()
                if page_text:
                    self.extracted_text += page_text + '\n'
                else:
                    print(f"No text found on page {i + 1}.")
                # Schedule progress bar update in main thread
                progress = (i + 1) / total_pages
                self.after(0, self.progress_bar.set, progress)
        self.after(0, self.progress_bar.set, 0)
        self.after(0, messagebox.showinfo, "PDF Loaded", "PDF text successfully extracted!")
    except Exception as e:
        print(f"An error occurred: {e}")
        self.after(0, messagebox.showerror, "Error", f"An error occurred: {e}")

