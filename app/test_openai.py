"""
Test script for OpenAI API connectivity.
"""
import os
from dotenv import load_dotenv
import openai

# Load .env file
load_dotenv()

# Set API key
api_key = os.getenv('OPENAI_API_KEY')
print(f"API key found: {'Yes' if api_key else 'No'}")
openai.api_key = api_key

try:
    # Simple test request
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Say hello world"}
        ]
    )
    print("\nAPI TEST SUCCESS!")
    print(f"Response: {response.choices[0].message['content']}")
    
except Exception as e:
    print(f"\nAPI TEST FAILED: {str(e)}")
    print("\nPlease check your API key and internet connection.")
