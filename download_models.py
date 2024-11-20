import spacy
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, AutoModelForQuestionAnswering


from env.config import *

def download_models():
    # Download spaCy model
    print(f"Downloading spaCy model: {SPACY_MODEL}")
    spacy.cli.download(SPACY_MODEL)

    # Download Hugging Face models
    print(f"Downloading summarization model: {SUMMARIZATION_ADVANCED_MODEL}")
    AutoTokenizer.from_pretrained(SUMMARIZATION_ADVANCED_MODEL)
    AutoModelForSeq2SeqLM.from_pretrained(SUMMARIZATION_ADVANCED_MODEL)

    print(f"Downloading question-answering model: {QUESTION_ANSWERING_MODEL}")
    AutoTokenizer.from_pretrained(QUESTION_ANSWERING_MODEL)
    AutoModelForQuestionAnswering.from_pretrained(QUESTION_ANSWERING_MODEL)

if __name__ == "__main__":
    download_models()