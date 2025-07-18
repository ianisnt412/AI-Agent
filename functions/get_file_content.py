import os
from functions.config import CHAR_LIMIT

def get_file_content(working_directory, file_path):
    abs_full_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_full_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(abs_full_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        with open(abs_full_path, 'r', encoding='utf-8') as file:
            file_contents = file.read(CHAR_LIMIT)
            return f'{file_contents}\n\n[...File "{file_path}" truncated at {CHAR_LIMIT} characters' if len(file_contents) == CHAR_LIMIT else file_contents
    except Exception as e:
        return f"Error diplaying contents of file: {e}"