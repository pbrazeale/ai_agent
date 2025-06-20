from google.genai import types

from functions.get_files_info import schema_get_files_info, get_files_info
from functions.get_files_content import schema_get_file_content, get_file_content
from functions.run_python import schema_run_python_file, run_python
from functions.write_files import schema_write_file, write_file

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file,
    ]
)

def call_function(function_call_part, verbose=False):
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")

    working_directory="./calculator"

    functions = {
        "get_files_info": get_files_info,
        "get_files_content": get_file_content,
        "run_python": run_python,
        "write_files": write_file,
    }

    try:
        selected_function = functions[function_call_part.name]
        all_args = {"working_directory": working_directory, **function_call_part.args}
        function_call_result = selected_function(**all_args)
        if function_call_result.parts[0].function_response.response:
            if verbose:
                print(f"-> {function_call_result.parts[0].function_response.response}")
            return types.Content(
                role="tool",
                parts=[
                    types.Part.from_function_response(
                        name=function_call_part.name,
                        response={"result": function_result},
                    )
                ],
            )
        else:
            raise Exception("Fatal Error no response")
    except KeyError:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call_part.name,
                    response={"error": f"Unknown function: {function_call_part.name}"},
                )
            ],
        )



