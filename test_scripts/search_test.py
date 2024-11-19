import os
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from env.device import get_device

# Suppress tokenizer parallelism warning
os.environ["TOKENIZERS_PARALLELISM"] = "false"

# Define device using your existing get_device function
DEVICE = get_device()

# Initialize Falcon model and tokenizer for question-answering
tokenizer = AutoTokenizer.from_pretrained("tiiuae/falcon-7b-instruct")
model = AutoModelForCausalLM.from_pretrained("tiiuae/falcon-7b-instruct", torch_dtype=torch.float16)
model.to(DEVICE)

def answer_question(content, question, keyword_match_threshold=0.1):
    # Simple keyword-based similarity check
    content_words = set(content.lower().split())
    question_words = set(question.lower().split())
    match_score = len(content_words.intersection(question_words)) / len(question_words)

    if match_score < keyword_match_threshold:
        return "I'm sorry, but I couldn't find relevant information in the document."

    # Generate answer using Falcon model
    prompt = f"Context: {content}\nQuestion: {question}\nAnswer:"
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512)
    inputs = {key: val.to(DEVICE) for key, val in inputs.items()}  # Move tensors to the correct device

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_length=150,
            num_return_sequences=1,
            no_repeat_ngram_size=2,  # Helps reduce repeated phrases
            early_stopping=True
        )

    # Decode the generated text
    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
    answer = answer.split("Answer:")[-1].strip()  # Extract the answer portion
    return answer