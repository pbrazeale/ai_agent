import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import *
from call_function import available_functions, call_function

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
    config=types.GenerateContentConfig(
        tools=[available_functions],
        system_instruction=system_prompt
    ),
)

if response.function_calls:
    for function_call_part in response.function_calls:
        # print(f"Calling function: {function_call_part.name}({function_call_part.args})")
        function_call_result = call_function(function_call_part, verbose)
        if function_call_result.parts[0].function_response.response:
            if verbose:
                print(f"-> {function_call_result.parts[0].function_response.response}")            
        else:
            raise Exception("Fatal Error no response")

if verbose:
    print(f"User prompt: {user_prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
