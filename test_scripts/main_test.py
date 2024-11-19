<<<<<<< HEAD
from extractor_test import extract_text_from_pdf
from summarize_test import summarizer
from search_test import answer_question


def test_extraction(file_path):
    print("Step 1. Testing Text Extractor")
    try:
        extracted_text = extract_text_from_pdf(file_path)
        print(extracted_text)
    except Exception as e:
        print(f"Error in text extraction: {e}")
        return None
=======
from extractor_test import *
from summarize_test import *

def main():
    #Step 1. Testing if text extraction works
    print("Step 1. Testing Text Extractor")
    extracted_text = extract_text_from_pdf("./files/Recommendation_Report copy.pdf")
    print(extracted_text)

>>>>>>> parent of 3bd35bf (Trying to implement llm for conversational questions)
    print("\n")
    return extracted_text

<<<<<<< HEAD

def test_summarization(extracted_text):
=======
    #Step 2. Testing text summarization
>>>>>>> parent of 3bd35bf (Trying to implement llm for conversational questions)
    print("Step 2. Testing Summarization Extractor")
    try:
        summarized_text = summarizer(extracted_text)
        print(summarized_text)
    except Exception as e:
        print(f"Error in summarization: {e}")
        return None
    print("\n")
    return summarized_text

<<<<<<< HEAD

def test_question_answering(extracted_text):
    print("Step 3. Ask questions based on PDF content")
    while True:
        question = input("Enter your question (or type 'exit' to quit): ")
        if question.lower() == "exit":
            break
        try:
            answer = answer_question(extracted_text, question)
            print(f"Answer: {answer}\n")
        except Exception as e:
            print(f"Error in question-answering: {e}")


def main():
    file_path = "./files/Recommendation_Report copy.pdf"

    # Step 1: Text Extraction
    extracted_text = test_extraction(file_path)
    if extracted_text is None:
        print("Extraction failed. Exiting.")
        return

    # Step 2: Summarization
    summarized_text = test_summarization(extracted_text)
    if summarized_text is None:
        print("Summarization failed. Exiting.")
        return

    # Step 3: Question Answering
    test_question_answering(extracted_text)

=======
    
>>>>>>> parent of 3bd35bf (Trying to implement llm for conversational questions)

if __name__ == "__main__":
    main()