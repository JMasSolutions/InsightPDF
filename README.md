

## InsightPDF


  
InsightPDF is a Python-based desktop application designed to provide a seamless and secure way to interact with PDF content directly on your device. With InsightPDF, you can upload PDFs, extract and summarize their content, and ask questions about specific information within the text—without needing an internet connection. This offline functionality ensures complete privacy and is especially useful for sensitive or confidential documents.  
  
**Features**  
  
 1. PDF Upload and Text Extraction  
  
    •  Upload PDFs: Easily upload a PDF document through the app’s intuitive interface.  
    •  Text Extraction: InsightPDF automatically extracts text from the uploaded PDF, allowing you to view, analyze, and interact with the content in various ways.  
  
 2. Summarization with BART-Large Model  
  
    •  Advanced Summarization: InsightPDF uses Facebook’s BART-Large model, a transformer-based language model fine-tuned for summarization tasks. This model efficiently condenses lengthy PDF content, capturing key points and saving you time.  
    •  High-Quality Summaries: Ideal for documents with dense information, BART-Large provides summaries that are both comprehensive and concise.  
  
 3. Q&A with RoBERTa Model  
  
    •  Ask Questions: InsightPDF is equipped with the RoBERTa (Robustly Optimized BERT Pretraining Approach) model, fine-tuned for question answering.  
    •  Instant Answers: Simply type your question about the content, and InsightPDF will quickly analyze the extracted text to provide a relevant response.  
  
**How It Works**  
  
 
 1. Load a PDF Document: Start by uploading your PDF file using the “Load PDF” button on the sidebar. 
 2. Text Extraction: InsightPDF extracts text from the PDF and displays it within the app. 
 3. Summarize Content: Click the “Summarize PDF” button to generate a summary of the extracted text using the BART-Large model. 
 4. Ask Questions: Enter a question in the Q&A section, and InsightPDF will provide an answer based on the document’s content using the RoBERTa model.  

**System Requirements**  
  

 - Platform: 
	 - Currently, InsightPDF is built for macOS (ARM64
   architecture). 
	 - Hardware:   
		 - Apple Silicon (Any of the M series chips) is required for optimal performance. 
	 - Memory: 
		 - Minimum of 7GB of RAM is recommended, as the summarization and Q&A models are resource-intensive. 
	

	 - Models and Libraries: 
		 - The app utilizes pre-trained models and libraries: 
			 - Summarization Model:
				 - facebook/bart-large-cnn (BART-Large). 
			- Question-Answering Model:
				- deepset/roberta-base-squad2 (RoBERTa). 
		- Libraries: 
		- The app requires pdfplumber, spacy, transformers, torch, and customtkinter.  
    
 ***Note: InsightPDF is currently distributed as a macOS executable, packaged using PyInstaller.*** 

**To run the application:**  

 - Download the InsightPDF App: 
	 - Download the latest version of the .app file. 
 - Move to Applications Folder: 
	 - Drag and drop the app into your Applications folder for easy access. 
 - Open the App: 
	 - Double-click InsightPDF.app to start the application. (On the first run, you may need to right-click and select “Open” due to macOS security settings.)  

**Usage**  
  
 - Start the Application: Open InsightPDF from your Applications folder. 
 - Load PDF: Click on “Load PDF” in the sidebar to select and upload a PDF document. 
 - Extract and Interact: 
	 •  Summarize: After loading the PDF, click “Summarize PDF” to generate a concise summary.
	•  Ask a Question: Type any question related to the document’s content, and the app will provide an answer based on the extracted text.  

**Privacy and Security**  
  
InsightPDF operates entirely offline. All processing, including text extraction, summarization, and question-answering, occurs locally on your device. No internet connection is required after the initial model downloads, ensuring the privacy of sensitive information.  
  
**Limitations**  
  

 - Platform Support: 
	 - Currently available only for macOS ARM64 (Apple   
   Silicon). Support for other platforms may be added in future   
   releases.     
   
 - Resource Usage: 
	 - InsightPDF uses machine learning   
   models that are resource-intensive, so a minimum of 16gb of RAM is   
   recommended to ensure smooth operation during summarization and Q&A  
 tasks.
       - During load InsightPDF will require a maximum of 6gb of RAM


