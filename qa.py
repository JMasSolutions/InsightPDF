import os
from transformers import pipeline

from env import DEVICE_INFO
from env.config import QUESTION_ANSWERING_MODEL

# Suppress the tokenizer parallelism warning
os.environ["TOKENIZERS_PARALLELISM"] = "false"

# Initialize the QA model with deepset/roberta-base-squad2
qa_model = pipeline(
    "question-answering",
    model=QUESTION_ANSWERING_MODEL,
    tokenizer=QUESTION_ANSWERING_MODEL,
    framework="pt",
    device=DEVICE_INFO
)

def get_answer(question, context):
    # Use the qa_model to get the answer
    answer = qa_model(question=question, context=context)
    return answer