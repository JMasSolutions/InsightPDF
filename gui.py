#gui.py

import customtkinter as ctk
from tkinter import filedialog, messagebox
from scripts.qa import get_answer
from scripts.summarize import summarize_text_advanced
import threading
from scripts.pdf_extractor import extract_text_with_progress

# Set the appearance and scaling
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")

class BasicApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configure the main window
        self.title("InsightPDF")
        self.geometry("800x600")
        self.resizable(False, False)

        # Center the window
        self.update_idletasks()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - 800) // 2  # 800 is the window width
        y = (screen_height - 600) // 2  # 600 is the window height
        self.geometry(f"800x600+{x}+{y}")

        # Sidebar Frame on the left for buttons with background color
        self.sidebar_frame = ctk.CTkFrame(self, width=200, corner_radius=10)
        self.sidebar_frame.pack(side="left", fill="y", padx=(20, 10), pady=20)

        # Sidebar Buttons
        self.load_pdf_button = ctk.CTkButton(
            self.sidebar_frame, text="Load PDF", command=self.open_pdf,
            font=("Arial", 14, "bold"), corner_radius=8
        )
        self.load_pdf_button.pack(pady=10, padx=10, fill="x")

        self.summarize_button = ctk.CTkButton(
            self.sidebar_frame, text="Summarize PDF", command=self.summarize_pdf_advanced,
            font=("Arial", 14, "bold"), corner_radius=8
        )
        self.summarize_button.pack(pady=10, padx=10, fill="x")

        self.ask_button = ctk.CTkButton(
            self.sidebar_frame, text="Ask Question", command=self.ask_question,
            font=("Arial", 14, "bold"), corner_radius=8
        )
        self.ask_button.pack(pady=10, padx=10, fill="x")

        # Quit Button at the very bottom of the sidebar
        self.quit_button = ctk.CTkButton(
            self.sidebar_frame, text="Quit", command=self.quit,
            font=("Arial", 14, "bold"), corner_radius=8
        )
        self.quit_button.pack(side="bottom", pady=10, padx=10, fill="x")

        # Clear Button with the other main buttons
        self.clear_button = ctk.CTkButton(
            self.sidebar_frame, text="Clear", command=self.clear_content,
            font=("Arial", 14, "bold"), corner_radius=8
        )
        self.clear_button.pack(side="bottom",pady=10, padx=10, fill="x")

        # Status Label above the Quit button
        self.status_label = ctk.CTkLabel(
            self.sidebar_frame, text="Status: Ready", font=("Arial", 13, "bold"), text_color="white"
        )
        self.status_label.pack(side="bottom", pady=10, padx=0, fill="x")


        # Main Frame for displaying content
        self.main_frame = ctk.CTkFrame(self, corner_radius=10)
        self.main_frame.pack( side="right", fill="both", expand=True, padx=(10, 20), pady=20)

        # Summary Display with larger font for summaries
        self.summary_display = ctk.CTkTextbox(
            self.main_frame, width=500, height=250, corner_radius=10, font=("Arial", 15), wrap="word"
        )
        self.summary_display.pack(pady=(20, 10), padx=20, fill="both", expand=True)
        self.summary_display.configure(state="disabled")

        # Question Entry Box with larger font and height
        self.question_entry = ctk.CTkEntry(
            self.main_frame, placeholder_text="Ask a question about the PDF content",
            font=("Arial", 13), height=40, corner_radius=8
        )
        self.question_entry.pack(pady=(0, 10), padx=20, fill="x")

        # Answer Display Label with larger font and no "Answer:" prefix
        self.answer_display = ctk.CTkLabel(
            self.main_frame, text="", font=("Arial", 14), corner_radius=8,
            anchor="center"
        )
        self.answer_display.pack(pady=(10, 20), padx=20, fill="x")

        # Variables to store extracted and summarized text
        self.extracted_text = ""
        self.summarized_text = ""

    def open_pdf(self):
        # Select a PDF file
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if file_path:
            # Update status to show PDF loaded
            self.update_status("Status: PDF Loaded", "cyan")
            # Start extraction in a separate thread
            threading.Thread(target=self.extract_text_thread, args=(file_path,)).start()

    def extract_text_thread(self, file_path):
        try:
            self.extracted_text = ''
            # Call the extract_text_with_progress function from pdf_extractor.py
            def progress_callback(progress):
                pass  # No progress bar to update here
            self.extracted_text = extract_text_with_progress(file_path, progress_callback)
            # Update status when done
            self.after(0, lambda: self.update_status("Status: PDF Loaded", "cyan"))
            self.after(0, messagebox.showinfo, "PDF Loaded", "PDF text successfully extracted!")
        except Exception as e:
            print(f"An error occurred: {e}")
            self.after(0, messagebox.showerror, "Error", f"An error occurred: {e}")

    def summarize_pdf_advanced(self):
        if self.extracted_text:
            # Update status to show summarizing
            self.update_status("Status: Summarizing...", "yellow")
            # Perform advanced summarization in a separate thread
            threading.Thread(target=self.summarize_thread, args=(True,)).start()
        else:
            messagebox.showwarning("No Text", "Please load a PDF first.")

    def summarize_thread(self, advanced=False):
        if advanced:
            self.summarized_text = summarize_text_advanced(self.extracted_text)
        else:
            self.summarized_text = summarize_text_advanced(self.extracted_text)
        # Update the summary display in the main thread
        self.after(0, self.update_summary_display)
        # Update status to PDF loaded after summarizing
        self.after(0, lambda: self.update_status("Status: PDF Loaded", "cyan"))

    def update_summary_display(self):
        self.summary_display.configure(state="normal")
        self.summary_display.delete("1.0", "end")
        self.summary_display.insert("1.0", self.summarized_text)
        self.summary_display.configure(state="disabled")

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
        # Display the answer directly, with larger font
        self.answer_display.configure(text=answer['answer'])

    def clear_content(self):
        """Clears the loaded PDF, summary, question, and response fields."""
        self.extracted_text = ""
        self.summarized_text = ""
        self.summary_display.configure(state="normal")
        self.summary_display.delete("1.0", "end")
        self.summary_display.configure(state="disabled")
        self.question_entry.delete(0, "end")
        self.answer_display.configure(text="")
        self.update_status("Status: No PDF Loaded", "red")

    def update_status(self, text, color):
        """Helper function to update the status text and color."""
        self.status_label.configure(text=text, text_color=color)

    def quit(self):
        self.destroy()

if __name__ == "__main__":
    app = BasicApp()
    app.mainloop()