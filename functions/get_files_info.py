import os

def get_files_info(working_directory, directory=None):
    abs_path = os.path.abspath(directory)

    if abs_path.startswith(working_directory) == False:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if os.path.isdir(directory) == False:
        return f'Error: "{directory}" is not a directory'

    if os.path.isdir(directory):
        try:
            dir_contents = os.listdir(directory)
        except Exception as e:
            return f"Error: {str(e)}"
    
        dir_formated_string = f""
    
        try:
            for item in dir_contents:
                dir_formated_string + f"- {item}: file_size={os.path.getsize(item)}, is_dir={os.path.isdir(item)}\n"
        except Exception as e:
            return f"Error: {str(e)}"
    
        return dir_formated_string
        '''
        - README.md: file_size=1032 bytes, is_dir=False
        - src: file_size=128 bytes, is_dir=True
        - package.json: file_size=1234 bytes, is_dir=False
        '''
