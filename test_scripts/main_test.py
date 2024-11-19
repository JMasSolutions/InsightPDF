from extractor_test import *
from summarize_test import *

def main():
    #Step 1. Testing if text extraction works
    print("Step 1. Testing Text Extractor")
    extracted_text = extract_text_from_pdf("./files/Recommendation_Report copy.pdf")
    print(extracted_text)

    print("\n")

    #Step 2. Testing text summarization
    print("Step 2. Testing Summarization Extractor")
    summarized_text = summarizer(extracted_text)
    print(summarized_text)

    print("\n")

    

if __name__ == "__main__":
    main()