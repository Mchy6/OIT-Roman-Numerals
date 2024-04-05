import unittest
from r_numeral_functions import _convert_to_int_list


class test_convert_to_list(unittest.TestCase):

    def test_convert_to_list(self):
        int_list = _convert_to_int_list("IVXLCDM")
        self.assertEqual([0, 1, 2, 3, 4, 5, 6], int_list)


if __name__ == '__main__':
    unittest.main()
