from transformers import pipeline
from env.config import SUMMARIZATION_MODEL

# Initialize the summarizer with PyTorch
summarizer = pipeline('summarization', model=SUMMARIZATION_MODEL, framework='pt')

def summarize_text(text, max_chunk_length=500):
    # Summarizes extracted content in a max of 324 words.
    text = text.replace('\n', ' ')
    summaries = []
    for i in range(0, len(text), max_chunk_length):
        chunk = text[i:i+max_chunk_length]
        summary = summarizer(chunk, max_length=512, min_length=40, do_sample=False)
        summaries.append(summary[0]['summary_text'])
    return ' '.join(summaries)