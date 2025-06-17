import os

def get_files_info(working_directory, directory=None):
    # list_working_dir = os.listdir(working_directory)
    working_dir_path = os.path.abspath(working_directory)
    if directory:
        target_path = os.path.join(os.path.abspath(working_directory), directory)
    else:
        target_path = working_dir_path
    # print(target_path)
    # print(os.path.abspath(working_directory))

    if target_path.startswith(working_dir_path) == False:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'    
    
    if os.path.isdir(target_path) == False:
        return f'Error: "{directory}" is not a directory'
    else:
        # print(os.listdir(target_path))
        try:
            dir_contents = os.listdir(target_path)
        except Exception as e:
            return f"Error: {str(e)}"
    
        dir_contents_formatted = []
    
        try:
            for item in dir_contents:
                item_path = os.path.join(target_path, item)
                dir_contents_formatted.append(f"- {item}: file_size={os.path.getsize(item_path)}, is_dir={os.path.isdir(item_path)}") 
        except Exception as e:
            return f"Error: {str(e)}"
        
        # print(dir_contents_formated)
        return f"\n".join(dir_contents_formatted)