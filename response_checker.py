from utils import load_api_key
import google.generativeai as genai
from typing import Tuple

def check_response(question: dict, user_response: str) -> Tuple[bool, str]:
    api_key = load_api_key()
    if not api_key:
        return False, "Error: API key not found. Please check your .env file."
    
    # Configure the genai library with your API key
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

    # Check if the user's response is correct
    is_correct = user_response.strip().lower() == question['answer'].strip().lower()
    
    if is_correct:
        return True, "Correct!"
    else:
        # Generate an explanation for the correct answer
        prompt = f"Explain why the correct answer to the question '{question['task']}' is '{question['answer']}' and why the user's answer '{user_response}' is incorrect very concisely."
        try:
            response = model.generate_content(prompt)
            explanation = response.text
            return False, explanation
        except Exception as e:
            return False, f"Error generating explanation: {str(e)}"