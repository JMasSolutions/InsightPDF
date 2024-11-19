import os
from transformers import pipeline
from env import DEVICE_INFO

# Suppress the tokenizer parallelism warning
os.environ["TOKENIZERS_PARALLELISM"] = "false"

# Initialize device
DEVICE_INFO = DEVICE_INFO

def llm_model():
    # Initialize a more consistent question-answering model
    qa_model = pipeline("question-answering", model="bert-large-uncased-whole-word-masking-finetuned-squad", framework="pt", device=DEVICE_INFO)
    return qa_model
