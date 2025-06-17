import os

def get_files_info(working_directory, directory=None):
    root_dir = os.listdir(working_directory)
    print(f"{os.path.abspath(working_directory)}/{working_directory}/{directory}")

    if directory not in root_dir:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory\n'
    
    if os.path.isdir(directory) == False:
        return f'Error: "{directory}" is not a directory\n'

    if os.path.isdir(f"{os.path.abspath(working_directory)}/{working_directory}/{directory}"):
        try:
            dir_contents = os.listdir(directory)
        except Exception as e:
            return f"Error: {str(e)}\n"
    
        dir_formated_string = f""
    
        try:
            for item in dir_contents:
                dir_formated_string + f"- {item}: file_size={os.path.getsize(item)}, is_dir={os.path.isdir(item)}\n"
        except Exception as e:
            return f"Error: {str(e)}\n"
    
        return dir_formated_string
        '''
        - README.md: file_size=1032 bytes, is_dir=False
        - src: file_size=128 bytes, is_dir=True
        - package.json: file_size=1234 bytes, is_dir=False
        '''
