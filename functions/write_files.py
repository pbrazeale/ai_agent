import os

def write_file(working_directory, file_path, content):
    working_dir_path = os.path.abspath(working_directory)
    target_path = os.path.abspath(os.path.join(os.path.abspath(working_directory), file_path))

    if not target_path.startswith(working_dir_path):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'      

    try:
        target_dir = os.path.dirname(target_path)
        if target_dir != "":
            if not os.path.exists(target_dir):
                os.makedirs(target_dir)

        with open(target_path, "w") as f:
            f.write(content)
            f.close()
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {str(e)}"

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write to the provided file.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Write to the provided file. If not provided, create the file and write to it.",
            ),
        },
    ),
)
