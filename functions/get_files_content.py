import os
from google.genai import types

MAX_CHARS = 10000

def get_file_content(working_directory, file_path):
    working_dir_path = os.path.abspath(working_directory)
    target_path = working_dir_path
    if file_path:
        target_path = os.path.abspath(os.path.join(os.path.abspath(working_directory), file_path))
    # print(target_path)
    # print(os.path.abspath(working_directory))

    if not target_path.startswith(working_dir_path):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'      
    if not os.path.isfile(target_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        with open(target_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if len(file_content_string) == 10000: 
                file_content_string += f'\n[...File "{file_path}" truncated at 10000 characters]'
            f.close()
        return file_content_string
    except Exception as e:
        return f"Error: {str(e)}"

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Read the contents of the file.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to read the contents from.",
            ),
        },
    ),
)
