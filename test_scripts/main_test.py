from extractor_test import *
from summarize_test import *
from search_test import *


def main():
    file_path = "./files/Recommendation_Report copy.pdf"

    # Step 1. Testing text extraction
    print("Step 1. Testing Text Extractor")
    extracted_text = extract_text_from_pdf(file_path)
    print(extracted_text)

    print("\n")

    # Step 2. Testing text summarization
    print("Step 2. Testing Summarization Extractor")
    summarized_text = summarizer(extracted_text)
    print(summarized_text)

    print("\n")

    # Step 3. Ask questions using the LLM with extracted text as context
    print("Step 3. Ask questions based on PDF content")
    while True:
        question = input("Enter your question (or type 'exit' to quit): ")
        if question.lower() == "exit":
            break

        # Get answer or handle unmatched query
        answer = answer_question(extracted_text, question)
        print(f"Answer: {answer}\n")


if __name__ == "__main__":
    main()