import os

def write_file(working_directory, file_path, content):
    abs_full_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_full_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    if os.path.exists(abs_full_path) and os.path.isdir(abs_full_path):
        return f'Error: "{file_path} is a directory, not a file'
    
    try:
        file_path_directory = os.path.dirname(abs_full_path)
        if not os.path.exists(file_path_directory):
            os.makedirs(file_path_directory)
    except Exception as e:
        return f"Error: Unable to create directory: {e}"
    
    try:
        with open(abs_full_path, "w") as file:
            file.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: Unable to write to "{file_path}": {e}'