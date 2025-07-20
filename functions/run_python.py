import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    abs_full_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_full_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(abs_full_path):
        return f'Error: File "{file_path}" not found'

    if not abs_full_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
  

    try:
        commands = ["uv", "run", abs_full_path]
        if args:
            commands.extend(args)
        result = subprocess.run(commands, capture_output=True, cwd=os.path.dirname(abs_full_path), timeout=30, text=True)
        output = []
        if result.stdout:
            output.append(f"STDOUT:\n{result.stdout}")
        if result.stderr:
            output.append(f"STDERR:\n{result.stderr}")
        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")
         
        return "\n".join(output) if output else "No output produced"
    except Exception as e:
        return f"Error: executing Python file: {e}"