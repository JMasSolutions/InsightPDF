# download_models.py
import os
import spacy
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, AutoModelForQuestionAnswering

SPACY_MODEL = 'en_core_web_sm'
SUMMARIZATION_ADVANCED_MODEL = 'facebook/bart-large-cnn'
QUESTION_ANSWERING_MODEL = 'deepset/roberta-base-squad2'

def download_models():
    # Download spaCy model
    if not spacy.util.is_package(SPACY_MODEL):
        print(f"Downloading spaCy model: {SPACY_MODEL}")
        spacy.cli.download(SPACY_MODEL)
    else:
        print(f"spaCy model '{SPACY_MODEL}' already installed.")

    # Download Hugging Face models if they don’t exist
    model_path = os.path.expanduser("~/.cache/huggingface/transformers")

    if not os.path.isdir(os.path.join(model_path, SUMMARIZATION_ADVANCED_MODEL)):
        print(f"Downloading summarization model: {SUMMARIZATION_ADVANCED_MODEL}")
        AutoTokenizer.from_pretrained(SUMMARIZATION_ADVANCED_MODEL)
        AutoModelForSeq2SeqLM.from_pretrained(SUMMARIZATION_ADVANCED_MODEL)
    else:
        print(f"Summarization model '{SUMMARIZATION_ADVANCED_MODEL}' already downloaded.")

    if not os.path.isdir(os.path.join(model_path, QUESTION_ANSWERING_MODEL)):
        print(f"Downloading question-answering model: {QUESTION_ANSWERING_MODEL}")
        AutoTokenizer.from_pretrained(QUESTION_ANSWERING_MODEL)
        AutoModelForQuestionAnswering.from_pretrained(QUESTION_ANSWERING_MODEL)
    else:
        print(f"Question-answering model '{QUESTION_ANSWERING_MODEL}' already downloaded.")

if __name__ == "__main__":
    download_models()