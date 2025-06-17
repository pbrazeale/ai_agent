import os

def get_files_info(working_directory, directory=None):
    # list_working_dir = os.listdir(working_directory)
    working_dir_path = os.path.abspath(working_directory)
    target_path = working_dir_path
    if directory:
        target_path = os.path.abspath(os.path.join(os.path.abspath(working_directory), directory))
    # print(target_path)
    # print(os.path.abspath(working_directory))

    if not target_path.startswith(working_dir_path):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'      
    if not os.path.isdir(target_path):
        return f'Error: "{directory}" is not a directory'
  
    # print(os.listdir(target_path))
    try:
        dir_contents_formatted = [] 
        for item in os.listdir(target_path):
            item_path = os.path.join(target_path, item)
            dir_contents_formatted.append(f"- {item}: file_size={os.path.getsize(item_path)}, is_dir={os.path.isdir(item_path)}") 
        # print(dir_contents_formated)
        return f"\n".join(dir_contents_formatted)
    except Exception as e:
        return f"Error: {str(e)}"
    