import os

def write_file(working_directory, file_path, content):
    working_dir_path = os.path.abspath(working_directory)
    target_path = os.path.abspath(os.path.join(os.path.abspath(working_directory), file_path))

    if not target_path.startswith(working_dir_path):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'      

    try:
        if not os.path.exists(target_path):
            os.makedirs(target_path)

        with open(target_path, "w") as f:
            f.write(content)
            f.close()
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {str(e)}"
