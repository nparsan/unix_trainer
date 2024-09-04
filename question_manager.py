import json
import random
from typing import List, Dict
from create_questions import generate_questions
import config

def load_questions() -> List[Dict]:
    try:
        with open('data/questions.json', 'r') as f:
            questions = json.load(f)
        return questions
    except FileNotFoundError:
        print("Error: questions.json file not found.")
        return []
    except json.JSONDecodeError:
        print("Error: Invalid JSON in questions.json file.")
        return []

def save_questions(questions: List[Dict]):
    with open('data/questions.json', 'w') as f:
        json.dump(questions, f, indent=2)

def select_questions(difficulty: str, num_questions: int, used_questions: List[str]) -> List[Dict]:
    all_questions = load_questions()
    if not all_questions:
        return []
    
    filtered_questions = [q for q in all_questions if q['difficulty'] == difficulty and q['task'] not in used_questions]
    
    if len(filtered_questions) < num_questions:
        new_questions = generate_questions(config.QUESTIONS_TO_GENERATE)
        new_filtered_questions = [q for q in new_questions if q['difficulty'] == difficulty and q['task'] not in used_questions]
        filtered_questions.extend(new_filtered_questions)
        all_questions.extend(new_questions)
        save_questions(all_questions)
    
    selected_questions = random.sample(filtered_questions, min(num_questions, len(filtered_questions)))
    return selected_questions

def mark_question_as_used(question: Dict, used_questions: List[str]):
    used_questions.append(question['task'])