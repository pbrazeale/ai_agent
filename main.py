import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

user_prompt = input("Enter your prompt:\n")

response = client.models.generate_content(
    model='gemini-2.0-flash-001',
    contents=f"{user_prompt}"
)

print(response.text)

print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
print(f"Prompt tokens: {response.usage_metadata.candidates_token_count}")
