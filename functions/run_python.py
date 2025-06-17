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
        completed = subprocess.run(target_path, capture_output=True, timeout=30,)
        if completed:
            formated_output = f"STDOUT: {completed.stdout}\n"
            formated_output += f"STDERR: {completed.stderr}"
            if completed.returncode != 0:
                formated_output += f"\nProcess exited with code {completed.returncode}"

            return formated_output
        else:
            return "No output produced."
    except Exception as e:
        return f"Error: executing Python file: {e}"
    
