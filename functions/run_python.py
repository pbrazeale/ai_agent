import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path):
    working_dir_path = os.path.abspath(working_directory)
    target_path = working_dir_path
    if file_path:
        target_path = os.path.abspath(os.path.join(os.path.abspath(working_directory), file_path))
    
    if not target_path.startswith(working_dir_path):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_path):
        return f'Error: File "{file_path}" not found.'
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        completed = subprocess.run(["python3", target_path], capture_output=True, timeout=30, text=True)
        if completed.stdout.strip() == "" and completed.stderr.strip() == "":
            return "No output produced."
        
        formated_output = f"STDOUT: {completed.stdout.strip()}\n"
        formated_output += f"STDERR: {completed.stderr.strip()}"
        if completed.returncode != 0:
            formated_output += f"\nProcess exited with code {completed.returncode}"    

        return formated_output
            
    except Exception as e:
        return f"Error: executing Python file: {e}"
    
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs the provided python file.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Runs the provided python file.",
            ),
        },
    ),
)
