# import unittest
# from functions.write_files import write_file 
from functions.run_python import run_python_file

def test():
    # result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    # print("Result for lorem.txt")
    # print(result)
    # print("")

    # result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    # print("Result for pkg/morelorem.txt")
    # print(result)
    # print("")

    # result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    # print("Result for /tmp/temp.txt")
    # print(result)
    # print("")

    result = run_python_file("calculator", "main.py")
    print("Result for running main.py")
    print(result)
    print("")    

    result = run_python_file("calculator", "tests.py")
    print("Result for running tests.py")
    print(result)
    print("")

    result = run_python_file("calculator", "../main.py")
    print("Result for running ../main.py")
    print(result)
    print("")

    result = run_python_file("calculator", "nonexistent.py")
    print("Result for running nonexistent.py")
    print(result)
    print("")



if __name__ == "__main__":
    test()