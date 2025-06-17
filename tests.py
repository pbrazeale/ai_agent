# import unittest
from functions.get_files_info import get_files_info

# Testing get_files_info 
# test_calculator_current
result1 = get_files_info("calculator", ".")
print(result2)

# test_calculator_pkg
result2 = get_files_info("calculator", "pkg")
print(result2)
    # self.assertEqual(result, "")

# test_calculator_bin
result3 = get_files_info("calculator", "/bin")
print(result3)

# test_calculator_parent
result4 = get_files_info("calculator", "../")
print(result4)


# if __name__ == "__main__":
#     unittest.main()
