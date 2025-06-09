import os
import sys
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

if api_key is None:
    print("Error: GEMINI_API_KEY not found in environment variables.")
    print("Please check your .env file and ensure it's in the same directory.")
    sys.exit(1)

client = genai.Client(api_key=api_key)

user_prompt = input("Enter your prompt:\n")

response = client.models.generate_content(
    model='gemini-2.0-flash-001',
    contents=f"{user_prompt}"
)

print(response.text)

print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
print(f"Prompt tokens: {response.usage_metadata.candidates_token_count}")
