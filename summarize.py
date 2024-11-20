import re
from transformers import pipeline, AutoTokenizer
from env.config import SUMMARIZATION_MODEL

# Initialize the tokenizer and summarizer
tokenizer = AutoTokenizer.from_pretrained(SUMMARIZATION_MODEL)
summarizer = pipeline('summarization', model=SUMMARIZATION_MODEL, framework='pt')


def split_into_sections(text):
    """
    Splits text into sections based on double line breaks or uppercase headers.
    This approach provides flexibility for documents with varied structures.
    """
    # Split by double line breaks or headers in uppercase
    sections = re.split(r'\n{2,}|\n[A-Z ]{3,}\n', text)

    # Clean up any extra whitespace
    sections = [section.strip() for section in sections if section.strip()]

    return sections


def summarize_text(text, max_chunk_length=300, overlap=50):
    """
    Summarizes the text by splitting it into manageable chunks and applying the summarization model to each chunk.
    Uses overlap between chunks to maintain context and prevent hallucinations.
    """
    summaries = []
    start = 0

    while start < len(text):
        end = min(start + max_chunk_length, len(text))
        chunk = text[start:end]

        # Tokenize and truncate to fit model's max token limit
        tokens = tokenizer(chunk, truncation=True, max_length=tokenizer.model_max_length, return_tensors="pt")
        input_length = tokens['input_ids'].shape[1]
        # minimize length
        # also check what the extracted text is being used

        # Set max_length for summarization dynamically based on chunk size
        max_length = min(100, input_length)
        min_length = max(30, max_length // 2)

        # Summarize the chunk
        summary = summarizer(chunk, max_length=max_length, min_length=min_length, do_sample=False)
        summaries.append(summary[0]['summary_text'])

        # Move the starting point, adding overlap for context
        start += max_chunk_length - overlap

    return ' '.join(summaries)


def summarize_by_sections(text, max_chunk_length=300, overlap=50):
    """
    Splits text into sections, summarizes each section, and combines them into a single summary.
    """
    # Split text into sections
    sections = split_into_sections(text)

    # Summarize each section individually
    final_summary = []
    for section in sections:
        section_summary = summarize_text(section, max_chunk_length=max_chunk_length, overlap=overlap)
        final_summary.append(section_summary)

    return ' '.join(final_summary)

