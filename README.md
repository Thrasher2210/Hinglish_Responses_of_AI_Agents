# Hinglish Voice AI

A project focused on building a conversational AI model that understands and responds in Hinglish (Hindi-English mix), using Google's Gemini API. This project aims to create natural, culturally appropriate responses that blend Hindi and English seamlessly.

## 🎯 Project Overview

This project implements a conversational AI that can naturally interact in Hinglish, combining the richness of Hindi with the technical precision of English. The implementation uses Google's Gemini API for generating contextually appropriate responses, with a focus on everyday conversational scenarios.

## 🛠️ Project Structure

- `inference.py`: Main script for generating responses using the Gemini API
- `context.json`: Contains the context and system prompts for the model
- `.env`: Environment variables (API keys)
- `requirements.txt`: Project dependencies

## 🚀 Setup

1. Clone the repository:
```bash
git clone [your-repo-url]
cd hinglish-voice-ai
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
Create a `.env` file with your Gemini API key:
```
GEMINI_API_KEY=your_api_key_here
```

## 🤖 Implementation Details

### Model Choice
- Using `gemini-1.5-flash` for its balance of speed and quality
- Temperature: 0.5 (balanced between creativity and consistency)
- Top-p: 0.95 (allows for diverse but relevant responses)
- Top-k: 50 (maintains response quality)
- Max output tokens: 50 (sufficient for concise responses)

### Context and Prompt Design
- Context is loaded from `context.json` to maintain conversation consistency
- Prompts follow a simple "User: [query]\nAssistant:" format
- Responses are cleaned to remove redundant "Assistant:" prefixes
- Error handling for API configuration and context loading

### Sample Prompts
```python
prompts = [
    "User: kal ke kya plans hai ?\nAssistant:",
    "User: Kaise ho bhai ? how are you doing ?\nAssistant:",
    "User: Bhai vo book padhke dimag ka shot crcuit ho gaya kuch tips dena?\nAssistant:"
]
```

## 📊 Evaluation

The model's performance is evaluated based on:
1. Response Relevance: How well the response matches the query context
2. Language Mix: Natural balance of Hindi and English
3. Cultural Appropriateness: Understanding of Indian context and idioms
4. Response Length: Concise and to-the-point answers
5. Error Handling: Robust error management for API and file operations

## 🔄 Future Improvements

1. Expand the context dataset with more diverse Hinglish examples
2. Implement a feedback mechanism for response quality
3. Add support for voice input/output
4. Create a web interface for easier interaction
5. Add support for more complex conversational scenarios
6. Implement response caching for better performance
7. Add support for different regional variations of Hinglish

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. When contributing:
1. Follow the existing code style
2. Add appropriate error handling
3. Include comments for complex logic
4. Update documentation as needed

## ⚠️ Important Notes

- Ensure your `.env` file is properly configured with the Gemini API key
- The `context.json` file must be present in the project root
- Responses are limited to 50 tokens for conciseness
- The model uses a balanced temperature setting for natural responses

## 🧠 Design Rationale

### Dataset Selection & Size
- Focused on everyday conversational scenarios (10-20 examples)
- Chose examples that represent common Hinglish usage patterns
- Included variations in language mixing (Hindi-heavy, English-heavy, balanced)
- Selected topics relevant to daily life (plans, greetings, advice)
- Examples demonstrate natural code-switching between Hindi and English

### Model & Hyperparameter Choices
- Selected `gemini-1.5-flash` for its:
  - Fast response times
  - Good understanding of mixed language inputs
  - Cost-effective for small-scale implementation
- Temperature (0.5): Balances creativity with consistency
- Top-p (0.95): Allows for diverse but relevant responses
- Top-k (50): Maintains response quality while allowing variety
- Max tokens (50): Ensures concise, focused responses

### Prompt Formatting & Generation Settings
- Simple "User: [query]\nAssistant:" format for clarity
- Consistent formatting across all examples
- Clear separation between user input and assistant response
- Error handling for API and file operations
- Response cleaning to remove redundant prefixes

### Quality Evaluation in Production
1. Human Review:
   - Native Hinglish speakers evaluate responses
   - Assess cultural appropriateness
   - Check language mixing balance
   - Verify response relevance

2. Automated Metrics:
   - Response length consistency
   - Error rate monitoring
   - API response time tracking
   - Language distribution analysis

3. User Feedback:
   - Collect user ratings
   - Track common issues
   - Monitor usage patterns
   - Gather improvement suggestions

## 📋 Sample Outputs

Example 1:
```
Prompt: User: kal ke kya plans hai ?
Response: Kal main shopping karne ja raha hoon, kuch new clothes lene hain. Aap bhi chaloge?
```

Example 2:
```
Prompt: User: Kaise ho bhai ? how are you doing ?
Response: Main mast hoon yaar! Work load thoda zyada hai but manage kar raha hoon. Aap kaise ho?
```

Example 3:
```
Prompt: User: Bhai vo book padhke dimag ka shot crcuit ho gaya kuch tips dena?
Response: Haha, samajh sakta hoon! Thoda break le lo, chai piyo aur fresh mind se padho. Small breaks are important for better understanding.
``` 
