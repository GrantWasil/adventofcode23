import re
import os 

script_dir = os.path.abspath(os.path.dirname(__file__))



total = 0
value = 0

digit_strings = {
    "one": '1',
    "two": '2',
    "three": '3',
    "four": '4', 
    "five": '5',
    "six": '6', 
    "seven": '7',
    "eight": '8',
    "nine": '9'
}

def parse_input_file(file_name):
    print("Parsing Input File: ", file_name)
    input_path = os.path.join(script_dir, file_name)
    content = ""
    with open(input_path, 'r') as f:
        content = f.read()
    return content

def ensure_valid_num(num):
    if num.isnumeric():
        return num
    else:
        return digit_strings[num]
    
def find_nums_in_line(line):
    print("Finding nums: ", line)
    pattern = "(?=(\d|one|two|three|four|five|six|seven|eight|nine))"
    digits = re.findall(pattern, line)
    return digits

def determine_digits(values):
    print("Determining Digits: ", values)
    if len(values) == 1:
        return [values[0], values[0]]
    return [values[0], values[-1]]

def validate_digits(digits):
    print("Validating Digits: ", digits)
    return [ensure_valid_num(digits[0]), ensure_valid_num(digits[1])]

def convert_to_values(digits):
    string_value = digits[0] + digits[1]
    return int(string_value)

def main():
    total = 0
    print("Starting Script")
    parsed_contnet = parse_input_file('input.txt')
    split_content = parsed_contnet.split("\n")
    for line in split_content:
        found_digits = find_nums_in_line(line)
        print("Found Digits: ", found_digits)
        if len(found_digits) < 1: 
            print("Line has no digits")
            break
        digits_to_use = determine_digits(found_digits)
        validated_digits = validate_digits(digits_to_use)
        converted_digits = convert_to_values(validated_digits)
        total += converted_digits

    print(total)

# split_content = content.split("\n")
# for line in split_content:
#     print("Line: ", line)
#     digits = re.findall("(\d|one|two|three|four|five|six|seven|eight|nine)", line)
#     print("Digits: ", digits)
#     if len(digits) < 1:
#         break
#     if len(digits) == 1:
#         valid_digit = ensure_valid_num(digits[0])
#         value = valid_digit + valid_digit
#     else:
#         value = ensure_valid_num(digits[0]) + ensure_valid_num(digits[-1])
#     print("Value is: ", value)
#     total += (int(value))
#     print("Current Total: ", total)

# print("Final Total: ", total)

if __name__ == '__main__':
    main()