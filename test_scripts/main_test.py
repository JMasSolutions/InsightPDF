from extractor_test import *

def main():
    #Step 1. Testing if text extraction works
    print("Step 1. Testing Text Extractor")
    result = extract_text_from_pdf("./files/Recommendation_Report copy.pdf")
    print(result)

if __name__ == "__main__":
    main()