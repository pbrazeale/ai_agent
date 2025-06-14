import unittest
from functions.get_files_info import get_files_info

# Testing get_files_info 
class TestCalculator(unittest.TestCase):
    def calculator_current(self):
        result = self.get_files_info("calculator", ".")
        print(result)
        # self.assertEqual(result, "")

    def calculator_pkg(self):
        result = self.get_files_info("calculator", "pkg")
        print(result)
        # self.assertEqual(result, "")

    def calculator_bin(self):
        result = self.get_files_info("calculator", "/bin")
        print(result)
        # self.assertEqual(result, "")

    def calculator_parent(self):
        result = self.get_files_info("calculator", "../")
        print(result)
        # self.assertEqual(result, "")



if __name__ == "__main__":
    unittest.main()
