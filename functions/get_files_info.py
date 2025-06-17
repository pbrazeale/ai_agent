import os

def get_files_info(working_directory, directory=None):
    root_dir = os.listdir(working_directory)
    working_dir_path = os.path.abspath(working_directory)
    target_path = working_dir_path.join(directory)
    # print(target_path)

    if directory not in root_dir:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory\n'
    
    if os.path.isdir(target_path) == False:
        return f'Error: "{directory}" is not a directory\n'
    else:
        # print(os.listdir(target_path))
        try:
            dir_contents = os.listdir(target_path)
        except Exception as e:
            return f"Error: {str(e)}\n"
    
        dir_contents_formated = f""
    
        try:
            for item in dir_contents:
                dir_contents_formated += f"- {item}: file_size={os.path.getsize(f"{target_path}/{item}")}, is_dir={os.path.isdir(f"{target_path}/{item}")}\n"
        except Exception as e:
            return f"Error: {str(e)}\n"
        
        # print(dir_contents_formated)
        return dir_contents_formated