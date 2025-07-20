import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from sys_prompt import system_prompt
from functions.schema_declaration import schema_get_files_info
from functions.schema_declaration import schema_get_file_content
from functions.schema_declaration import schema_run_python_file
from functions.schema_declaration import schema_write_file
from functions.schema_declaration import available_functions

def main():
    load_dotenv()
    
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    verbose = "--verbose" in sys.argv
    args = []
    for arg in sys.argv[1:]:
        if not arg.startswith("--"):
            args.append(arg)
    
    if len(sys.argv) < 2:
        print("Please enter a query")
        sys.exit(1)
    
    user_prompt = " ".join(args)
    
    if verbose:
        print(f"User prompt: {user_prompt} \n")
    
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]

    generate_content(client, messages, verbose)


def generate_content(client, messages, verbose):    
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', 
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt
        ),
    )
    
    if response.function_calls:
        for function_call in response.function_calls:
            print(f"Calling function: {function_call.name}({function_call.args})")
    print(f"Response:\n {response.text}")    
    if verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
