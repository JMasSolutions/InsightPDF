import os
import torch
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
from env.device import get_device

# Suppress tokenizer parallelism warning
os.environ["TOKENIZERS_PARALLELISM"] = "false"

# Define device using your existing get_device function
DEVICE = get_device()

# Initialize Falcon model and tokenizer for question-answering
tokenizer = AutoTokenizer.from_pretrained("tiiuae/falcon-7b-instruct")
model = AutoModelForCausalLM.from_pretrained("tiiuae/falcon-7b-instruct", device_map="auto", torch_dtype=torch.float16)

# Use pipeline with Falcon for conversational answering
qa_model = pipeline("text-generation", model=model, tokenizer=tokenizer, device=DEVICE)

def answer_question(content, question, keyword_match_threshold=0.1):
    # Simple keyword-based similarity check
    content_words = set(content.lower().split())
    question_words = set(question.lower().split())
    match_score = len(content_words.intersection(question_words)) / len(question_words)

    if match_score < keyword_match_threshold:
        # If similarity is below threshold, return no match found
        return "I'm sorry, but I couldn't find relevant information in the document."

    # Generate answer using Falcon model
    prompt = f"Context: {content}\nQuestion: {question}\nAnswer:"
    answer = qa_model(prompt, max_length=150, num_return_sequences=1)[0]["generated_text"]
    return answer

# Example usage
def main():
    # Sample content for testing
    content = "This is an example document discussing various topics such as climate change, technology, and history."
    question = "What is discussed in this document?"

    # Get answer or handle unmatched query
    answer = answer_question(content, question)
    print(f"Answer: {answer}\n")

if __name__ == "__main__":
    main()