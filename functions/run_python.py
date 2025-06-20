import os
import subprocess

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
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
