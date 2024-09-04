import google.generativeai as genai
from utils import load_api_key

def test_gemini_model():
    # Configure the genai library with your API key
    genai.configure(api_key=load_api_key())
    # Create a model instance
    model = genai.GenerativeModel('gemini-1.5-flash')

    # Define a simple prompt to test the model
    prompt = "What is the purpose of the 'ls' command in Linux?"

    try:
        # Generate content using the model
        response = model.generate_content(prompt)
        print("Response from gemini-1.5-flash:")
        print(response.text)
    except Exception as e:
        print(f"Error testing gemini-1.5-flash: {str(e)}")

# Call the test function
test_gemini_model()
