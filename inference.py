import google.generativeai as genai
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not set in .env file")

# Configure Gemini API
try:
    genai.configure(api_key=api_key)
except Exception as e:
    print(f"Error configuring API: {e}")
    exit()

# Load context
try:
    with open('context.json', 'r', encoding='utf-8') as f:
        context_data = json.load(f)
    context = context_data['context']
    print("Loaded context from context.json")
except Exception as e:
    print(f"Error loading context: {e}")
    exit()

# Initialize model
try:
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    print(f"Error initializing model: {e}")
    exit()

# Define prompts
prompts = [
    "User: kal ke kya plans hai ?\nAssistant:",
    "User: Kaise ho bhai ? how are you doing ?\nAssistant:",
    "User: Bhai vo book padhke dimag ka shot crcuit ho gaya kuch tips dena?\nAssistant:"
]

# Generate responses
for prompt in prompts:
    try:
        full_prompt = f"{context}\n{prompt}"
        response = model.generate_content(
            full_prompt,
            generation_config={
                "temperature": 0.5,
                "top_p": 0.95,
                "top_k": 50,
                "max_output_tokens": 50
            }
        )
        response_text = response.text.strip()
        cleaned_response = response_text if not response_text.startswith("Assistant:") else response_text.split("Assistant:")[-1].strip()
        print(f"Prompt: {prompt}")
        print(f"Raw Response: {response_text}")
        print(f"Cleaned Response: {cleaned_response}\n")
    except Exception as e:
        print(f"Error generating response for {prompt}: {e}")