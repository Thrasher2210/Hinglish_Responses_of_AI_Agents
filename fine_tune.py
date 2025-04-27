import json
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not set in .env file")

dataset = []
try:
    with open('dataset.jsonl', 'r', encoding='utf-8') as f:
        for line in f:
            dataset.append(json.loads(line.strip()))
    print(f"Loaded dataset with {len(dataset)} examples")
    print(f"First example: {dataset[0]}")
except Exception as e:
    print(f"Error loading dataset: {e}")
    exit()

context = "You are a Hinglish Voice AI assistant. Respond in casual, fluent Hinglish as shown in these examples:\n\n"
for example in dataset:
    context += f"{example['prompt']} {example['completion']}\n\n"

try:
    with open('context.json', 'w', encoding='utf-8') as f:
        json.dump({"context": context}, f, ensure_ascii=False, indent=2)
    print("Context saved to context.json")
except Exception as e:
    print(f"Error saving context: {e}")
    exit()