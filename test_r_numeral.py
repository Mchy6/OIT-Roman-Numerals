import unittest
from r_numeral_functions import _convert_to_int_list
from r_numeral_functions import check_input


class test_convert_to_list(unittest.TestCase):

    def test_convert_to_list(self):
        int_list = _convert_to_int_list("IVXLCDM")
        self.assertEqual([0, 1, 2, 3, 4, 5, 6], int_list)

class test_check_input(unittest.TestCase):

    def test_invalid_character(self):
        success: bool = check_input("IVa")[0]
        message: str = check_input("IVa")[1]
        self.assertEqual(success, False)
        self.assertEqual(message, "a is not a valid character.")

    def test_invalid_repetition_1(self):
        success: bool = check_input("MMMM")[0]
        message: str = check_input("MMMM")[1]
        self.assertEqual(success, False)
        self.assertEqual(message, "M cannot be repeated more than three times.")

    def test_invalid_repetition_2(self):
        success: bool = check_input("VV")[0]
        message: str = check_input("VV")[1]
        self.assertEqual(success, False)
        self.assertEqual(message, "V cannot be repeated more than once.")

    def test_invalid_subtractive_combination_1(self):
        success: bool = check_input("IC")[0]
        message: str = check_input("IC")[1]
        self.assertEqual(success, False)
        self.assertEqual(message, "C cannot be preceded by I")

    def test_invalid_subtractive_combination_2(self):
        success: bool = check_input("XD")[0]
        message: str = check_input("XD")[1]
        self.assertEqual(success, False)
        self.assertEqual(message, "D cannot be preceded by X")

    def test_empty_string(self):
        success: bool = check_input("")[0]
        message: str = check_input("")[1]
        self.assertEqual(success, False)
        self.assertEqual(message, "Empty string is not a valid Roman numeral.")

    def test_check_input_true(self):
        success: bool = check_input("IX")[0]
        message: str = check_input("IX")[1]
        self.assertEqual(success, True)
        self.assertEqual(message, "")

if __name__ == '__main__':
    unittest.main()
