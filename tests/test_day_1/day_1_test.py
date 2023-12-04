import unittest
from day_1 import ensure_valid_num, find_nums_in_line, determine_digits, validate_digits, convert_to_values

class TestDay1(unittest.TestCase):
    def test_ensure_valid_num(self):
        # Test to ensure textual numbers are correctly converted to numeric strings
        self.assertEqual(ensure_valid_num('one'), '1')
        self.assertEqual(ensure_valid_num('3'), '3')

    def test_find_nums_in_line(self):
        self.assertEqual(find_nums_in_line('two1nine'), ['two', '1', 'nine'])
        self.assertEqual(find_nums_in_line('abcone2threexyz'), ['one', '2', 'three'])
        self.assertEqual(find_nums_in_line('xtwone3four'), ['two', 'one', '3', 'four'])
        self.assertEqual(find_nums_in_line('4nineeightseven2'), ['4', 'nine', 'eight', 'seven', '2'])
        self.assertEqual(find_nums_in_line('7pqrstsixteen'), ['7', 'six'])

    def test_determine_digits(self):
        self.assertEqual(determine_digits(['two', '1', 'nine']), ['two', 'nine'])
        self.assertEqual(determine_digits(['one', '2', 'three']), ['one', 'three'])
        self.assertEqual(determine_digits(['7', 'six']), ['7', 'six'])
        self.assertEqual(determine_digits(['two']), ['two', 'two'])
    
    def test_validate_digits(self):
        self.assertEqual(validate_digits(['two', 'nine']), ['2', '9'])
        self.assertEqual(validate_digits(['one', 'three']), ['1', '3'])
        self.assertEqual(validate_digits(['7', 'six']), ['7', '6'])
        self.assertEqual(validate_digits(['two', 'two']), ['2', '2'])
    
    def test_convert_to_value(self):
        self.assertEqual(convert_to_values(['2', '9']), 29)
        self.assertEqual(convert_to_values(['1', '3']), 13)
        self.assertEqual(convert_to_values(['7', '6']), 76)
        self.assertEqual(convert_to_values(['2', '2']), 22)


if __name__ == '__main__':
    unittest.main()