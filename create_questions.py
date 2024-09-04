import google.generativeai as genai
from typing import List, Dict
from utils import load_api_key
import json
import requests
from tqdm import tqdm

def generate_questions(num_questions: int) -> List[Dict]:
    genai.configure(api_key=load_api_key())
    model = genai.GenerativeModel('gemini-1.5-flash', generation_config={"response_mime_type": "application/json"})

    prompt = f"""Generate {num_questions} questions about Linux shell navigation and shell scripting in JSON mode.
    For each question, provide:
    1. A task description
    2. The correct answer
    3. The difficulty level (easy, medium, or hard)
    
    Format the output as a JSON array of objects, each containing 'task', 'answer', and 'difficulty' keys."""

    try:
        response = model.generate_content(prompt)
        questions = response.text
        formatted_questions = json.loads(questions)
        return formatted_questions
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in the response.")
        return []
    except Exception as e:
        print(f"Error generating questions: {str(e)}")
        return []

def check_similarity(new_questions: List[Dict], existing_questions: List[Dict]) -> List[Dict]:
    similar_questions = []
    for new_question in new_questions:
        for existing_question in existing_questions:
            if is_similar(new_question, existing_question):
                similar_questions.append(new_question)
                break
    return [q for q in new_questions if q not in similar_questions]

def is_similar(question1: Dict, question2: Dict) -> bool:
    return question1['task'].strip().lower() == question2['task'].strip().lower()

def save_questions(questions: List[Dict]):
    try:
        with open('data/questions.json', 'r') as f:
            existing_questions = json.load(f)
    except FileNotFoundError:
        existing_questions = []

    unique_questions = check_similarity(questions, existing_questions)
    existing_questions.extend(unique_questions)

    with open('data/questions.json', 'w') as f:
        json.dump(existing_questions, f, indent=2)

def main(num_questions: int):
    api_key = load_api_key()
    if api_key:
        print("API Key loaded successfully.")
        all_questions = []
        
        # Chunking the requests into batches of 10
        for i in tqdm(range(0, num_questions, 10), desc="Generating questions"):
            batch_size = min(10, num_questions - i)  # Ensure we don't exceed the total
            questions = generate_questions(batch_size)
            all_questions.extend(questions)

        save_questions(all_questions)
        print(f"Saved {len(all_questions)} new questions.")
    else:
        print("Error: API Key is not valid or not found.")

if __name__ == "__main__":
    main(25)  