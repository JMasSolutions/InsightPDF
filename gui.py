# gui.py
import customtkinter as ctk
from tkinter import filedialog, messagebox
from qa import get_answer
from summarize import summarize_by_sections
import threading
from pdf_extractor import extract_text_with_progress

# Set the appearance and scaling
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")

class BasicApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configure the main window
        self.title("PDF Summarizer and Q&A App")
        self.geometry("600x700")

        # Title Label
        self.label = ctk.CTkLabel(self, text="Welcome to the PDF Summarizer and Q&A App!", font=("Arial", 16))
        self.label.pack(pady=10)

        # PDF Load Button
        self.load_pdf_button = ctk.CTkButton(self, text="Load PDF", command=self.open_pdf)
        self.load_pdf_button.pack(pady=10)

        # Progress Bar for PDF Extraction
        self.progress_bar = ctk.CTkProgressBar(self, width=500)
        self.progress_bar.pack(pady=10)
        self.progress_bar.set(0)

        # Button to Summarize PDF
        self.summarize_button = ctk.CTkButton(self, text="Summarize PDF", command=self.summarize_pdf)
        self.summarize_button.pack(pady=10)

        # Display Area for Summarized Text
        self.summary_display = ctk.CTkTextbox(self, width=500, height=150)
        self.summary_display.pack(pady=10)

        # Question Entry Box
        self.question_entry = ctk.CTkEntry(self, placeholder_text="Ask a question about the PDF content")
        self.question_entry.pack(pady=10)

        # Button to Ask Question
        self.ask_button = ctk.CTkButton(self, text="Ask Question", command=self.ask_question)
        self.ask_button.pack(pady=10)

        # Display Answer
        self.answer_display = ctk.CTkLabel(self, text="", font=("Arial", 12))
        self.answer_display.pack(pady=10)

        # Quit Button
        self.quit_button = ctk.CTkButton(self, text="Quit", command=self.quit)
        self.quit_button.pack(pady=10)

        # Variables to store extracted and summarized text
        self.extracted_text = ""
        self.summarized_text = ""

    def open_pdf(self):
        # Select a PDF file
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if file_path:
            # Start extraction in a separate thread
            threading.Thread(target=self.extract_text_thread, args=(file_path,)).start()

    def extract_text_thread(self, file_path):
        try:
            self.extracted_text = ''
            # Call the extract_text_with_progress function from pdf_extractor.py
            def progress_callback(progress):
                # Schedule the progress bar update in the main thread
                self.after(0, self.progress_bar.set, progress)
            self.extracted_text = extract_text_with_progress(file_path, progress_callback)
            # Reset the progress bar and show a message when done
            self.after(0, self.progress_bar.set, 0)
            self.after(0, messagebox.showinfo, "PDF Loaded", "PDF text successfully extracted!")
        except Exception as e:
            print(f"An error occurred: {e}")
            self.after(0, messagebox.showerror, "Error", f"An error occurred: {e}")

    def summarize_pdf(self):
        if self.extracted_text:
            # Perform summarization in a separate thread
            threading.Thread(target=self.summarize_thread).start()
        else:
            messagebox.showwarning("No Text", "Please load a PDF first.")

    def summarize_thread(self):
        self.summarized_text = summarize_by_sections(self.extracted_text)
        # Update the summary display in the main thread
        self.after(0, self.update_summary_display)

    def update_summary_display(self):
        self.summary_display.delete("1.0", "end")
        self.summary_display.insert("1.0", self.summarized_text)

    def ask_question(self):
        question = self.question_entry.get()
        if question and self.extracted_text:
            # Perform Q&A in a separate thread
            threading.Thread(target=self.get_answer_thread, args=(question,)).start()
        else:
            messagebox.showwarning("No Text or Question", "Please load a PDF and enter a question.")

    def get_answer_thread(self, question):
        answer = get_answer(question, self.extracted_text)
        # Update the answer display in the main thread
        self.after(0, self.update_answer_display, answer)

    def update_answer_display(self, answer):
        self.answer_display.configure(text=f"Answer: {answer['answer']}")

    def quit(self):
        self.destroy()

if __name__ == "__main__":
    app = BasicApp()
    app.mainloop()