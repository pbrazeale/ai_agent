import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

# user_prompt = input("Enter your prompt:\n")

# response = client.models.generate_content(
#     model='gemini-2.0-flash-001',
#     contents=f"{user_prompt}"
# )
try:
    user_prompt = sys.argv[1]
except:
    print('Provide prompt: python3 main.py "example prompt"')
    sys.exit(1)

try:
    if sys.argv[2] == '--verbose':
        verbose = True
except:
    verbose = False

messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]


response = client.models.generate_content(
    model='gemini-2.0-flash-001',
    contents=messages,
)

print(response.text)

if verbose:
    print(f"User prompt: {user_prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
