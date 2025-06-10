import os
import sys
from dotenv import load_dotenv
from google import genai

def main():
    load_dotenv("/.env")

    try:
        if len(sys.argv) == 1 or not isinstance(sys.argv[1], str):
            raise ValueError("Need a prompt | python3 main.py 'prompt'")
    except ValueError as e:
        print(e)
        sys.exit(1)

    prompt = sys.argv[1]

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)    

    response = client.models.generate_content(
                    model="gemini-2.0-flash-001",
                    contents=prompt)
    
    prompt_tokens = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.candidates_token_count

    print(f"Prompt tokens: {prompt_tokens}\nResponse tokens: {response_tokens}")
    print(f"Response: {response.text}")


if __name__ == "__main__":
    main()