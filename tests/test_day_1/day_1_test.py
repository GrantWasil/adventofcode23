import pytest

from day_1.day_1 import (
    convert_to_values,
    determine_digits,
    ensure_valid_num,
    find_nums_in_line,
    validate_digits,
)


class TestDay1:
    def test_ensure_valid_num(self):
        # Test to ensure textual numbers are correctly converted to numeric strings
        assert ensure_valid_num("one") == "1"
        assert ensure_valid_num("3") == "3"

    def test_find_nums_in_line(self):
        assert find_nums_in_line("two1nine") == ["two", "1", "nine"]
        assert find_nums_in_line("abcone2threexyz") == ["one", "2", "three"]
        assert find_nums_in_line("xtwone3four") == ["two", "one", "3", "four"]
        assert find_nums_in_line("4nineeightseven2") == [
            "4",
            "nine",
            "eight",
            "seven",
            "2",
        ]
        assert find_nums_in_line("7pqrstsixteen") == ["7", "six"]

    def test_determine_digits(self):
        assert determine_digits(["two", "1", "nine"]) == ["two", "nine"]
        assert determine_digits(["one", "2", "three"]) == ["one", "three"]
        assert determine_digits(["7", "six"]) == ["7", "six"]
        assert determine_digits(["two"]) == ["two", "two"]

    def test_validate_digits(self):
        assert validate_digits(["two", "nine"]) == ["2", "9"]
        assert validate_digits(["one", "three"]) == ["1", "3"]
        assert validate_digits(["7", "six"]) == ["7", "6"]
        assert validate_digits(["two", "two"]) == ["2", "2"]

    def test_convert_to_value(self):
        assert convert_to_values(["2", "9"]) == 29
        assert convert_to_values(["1", "3"]) == 13
        assert convert_to_values(["7", "6"]) == 76
        assert convert_to_values(["2", "2"]) == 22


if __name__ == "__main__":
    pytest.main()
