# qa.py
import os
from transformers import pipeline

# Suppress the tokenizer parallelism warning
os.environ["TOKENIZERS_PARALLELISM"] = "false"

# Initialize device (use CPU if DEVICE_INFO is not defined)
DEVICE_INFO = -1

# Initialize the QA model once
qa_model = pipeline(
    "question-answering",
    model="bert-large-uncased-whole-word-masking-finetuned-squad",
    framework="pt",
    device=DEVICE_INFO
)

def get_answer(question, context):
    # Use the qa_model to get the answer
    answer = qa_model(question=question, context=context)
    return answer