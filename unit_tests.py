import unittest
from find_seat import decode_boarding_pass, decode_row, decode_column

class BoardingPassDecodeTest(unittest.TestCase):

    def test_first_pass(self):
        self.assertEqual(decode_boarding_pass("BFFFBBFRRR"), (567, 70, 7))
    def test_second_pass(self):
        self.assertEqual(decode_boarding_pass("FFFBBBFRRR"), (119, 14, 7))
    def test_third_pass(self):
        self.assertEqual(decode_boarding_pass("BBFFBBFRLL"), (820, 102, 4))

    def test_invalid_pass_1(self):
        #Pass code too short
        with self.assertRaises(ValueError):
            decode_boarding_pass("BBFFBBFRL")
    
    def test_invalid_pass_2(self):
        #Pass code too long
        with self.assertRaises(ValueError):
            decode_boarding_pass("BBFFBBBFRLL")
    
    def test_invalid_pass_3(self):
        #Invalid characters in code
        with self.assertRaises(ValueError):
            decode_boarding_pass("BBFFBALPHA")

if __name__ == '__main__':
    unittest.main()