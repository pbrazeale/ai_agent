import os


def get_files_info(working_directory, directory=None):
    
    if directory not in working_directory:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if directory:
        pass
        '''
        - README.md: file_size=1032 bytes, is_dir=False
        - src: file_size=128 bytes, is_dir=True
        - package.json: file_size=1234 bytes, is_dir=False
        '''
    else:
        return f'Error: "{directory}" is not a directory'