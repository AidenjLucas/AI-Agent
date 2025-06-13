import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from call_functions import available_functions
from constants import system_prompt

def main():
    load_dotenv("/.env")

    try:
        if len(sys.argv) == 1 or not isinstance(sys.argv[1], str):
            raise ValueError("Need a prompt | python3 main.py 'prompt'")
    except ValueError as e:
        print(e)
        sys.exit(1)

    prompt = sys.argv[1]
    flags = sys.argv[1:]

    messages = [
    types.Content(role="user", parts=[types.Part(text=prompt)]),
    ]

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)    

    response = client.models.generate_content(
                    model="gemini-2.0-flash-001",
                    contents=messages,
                    config=types.GenerateContentConfig(tools=[available_functions],system_instruction=system_prompt))

    prompt_tokens = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.candidates_token_count

    if "--verbose" in flags:
        print(f"User prompt: {prompt}")
        print(f"Prompt tokens: {prompt_tokens}\nResponse tokens: {response_tokens}")

    if len(response.function_calls) != 0:
        for function in response.function_calls:
            print(f"Calling function: {function.name}({function.args})")

    print(f"Response:\n{response.text}")



if __name__ == "__main__":
    main()