import os
import re

script_dir = os.path.abspath(os.path.dirname(__file__))


def parse_input_file(file_name):
    print("Parsing Input File: ", file_name)
    input_path = os.path.join(script_dir, file_name)
    with open(input_path, "r") as f:
        content = f.read()
    return content


def main():
    print("Starting Script")
    parsed_content = parse_input_file("input.txt")
    split_content = parsed_content.split("\n")
    print(split_content)


if __name__ == "__main__":
    main()
