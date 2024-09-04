from dotenv import load_dotenv
import os
import re

def load_api_key():
    load_dotenv(override=True)  # Ensure environment variables are reloaded
    return os.getenv('GEMINI_API_KEY')

def sanitize_input(user_input):
    # Remove any potentially harmful characters or sequences
    sanitized = re.sub(r'[;&|]', '', user_input)
    # Remove leading/trailing whitespace
    sanitized = sanitized.strip()
    return sanitized