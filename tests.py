# import unittest
from functions.get_files_content import get_file_content 

def test():
    result = get_file_content("calculator", "lorem.txt")
    print("Result for lorem.txt")
    print(result)
    print("")


if __name__ == "__main__":
    test()