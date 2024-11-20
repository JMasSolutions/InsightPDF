from transformers import AutoTokenizer, pipeline

from env import DEVICE_INFO
from env.config import SUMMARIZATION_ADVANCED_MODEL

# Initialize the tokenizer and summarizer for the advanced model
advanced_tokenizer = AutoTokenizer.from_pretrained(SUMMARIZATION_ADVANCED_MODEL)
advanced_summarizer = pipeline('summarization', model=SUMMARIZATION_ADVANCED_MODEL, framework='pt', device=DEVICE_INFO)

def summarize_text_advanced(text):
    # Directly use the advanced_summarizer pipeline for summarization
    response = advanced_summarizer(text, max_length=150, min_length=50, do_sample=False)
    return response[0]['summary_text']



