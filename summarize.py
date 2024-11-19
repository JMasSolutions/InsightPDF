from transformers import pipeline, AutoTokenizer
from env.config import SUMMARIZATION_MODEL

# Initialize the tokenizer and summarizer
tokenizer = AutoTokenizer.from_pretrained(SUMMARIZATION_MODEL)
summarizer = pipeline('summarization', model=SUMMARIZATION_MODEL, framework='pt')

def summarize_text(text, max_chunk_length=200, overlap=50):
    text = text.replace('\n', ' ')
    summaries = []
    start = 0

    while start < len(text):
        end = min(start + max_chunk_length, len(text))
        chunk = text[start:end]

        # Adjust the max_length and min_length for the summary
        input_length = len(tokenizer.encode(chunk))
        max_length = min(100, input_length)  # Cap max length to avoid hallucinations
        min_length = max(30, max_length // 2)  # Reasonable min length based on max

        # Summarize the chunk
        summary = summarizer(chunk, max_length=max_length, min_length=min_length, do_sample=False)
        summaries.append(summary[0]['summary_text'])

        # Move the starting point with overlap
        start += max_chunk_length - overlap

    return ' '.join(summaries)