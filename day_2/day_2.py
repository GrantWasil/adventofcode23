import os
import re

script_dir = os.path.abspath(os.path.dirname(__file__))


def parse_input_file(file_name):
    print("Parsing Input File: ", file_name)
    input_path = os.path.join(script_dir, file_name)
    with open(input_path, "r") as f:
        content = f.read()
    return content


def validate_game(line):
    id_regex = "(Game )(\d+)"
    id = re.search(id_regex, line).group(2)
    cube_count = {"id": int(id), "blue": 0, "red": 0, "green": 0}
    results = line.split(":")[1]
    each_pull = results.split(";")
    for pull in each_pull:
        color_cubes = pull.split(",")
        for color_cube in color_cubes:
            num, color = re.search("(\d+) (\w+)", color_cube).groups()
            cube_count[color] += int(num)
    return cube_count


def format_input_data(line):
    id_regex = "(Game )(\d+)"
    id = re.search(id_regex, line).group(2)
    game_data = {"id": int(id), "total": 0}
    all_pulls = line.split(":")[1].split(";")
    for pull in all_pulls:
        game_data["total"] += 1
        current_pull_id = game_data["total"]
        current_cube_count = {"blue": 0, "red": 0, "green": 0}
        color_cubes = pull.split(",")
        for color_cube in color_cubes:
            num, color = re.search("(\d+) (\w+)", color_cube).groups()
            current_cube_count[color] += int(num)
        game_data[current_pull_id] = current_cube_count
    return game_data


def is_pull_valid(pull):
    max_cubes = {"blue": 14, "red": 12, "green": 13}
    for color in ["blue", "red", "green"]:
        if pull[color] > max_cubes[color]:
            return False
    return True


def find_minimum_amount_of_cubes(game):
    minimum_cubes = {"blue": 0, "red": 0, "green": 0}
    for i in range(1, game["total"] + 1):
        print("\t Checking Pull :", game[i])
        for color in ["red", "blue", "green"]:
            if game[i][color] > minimum_cubes[color]:
                minimum_cubes[color] = game[i][color]
    return minimum_cubes


def get_product_of_cubes(cubes):
    product = 1
    for color in ["red", "blue", "green"]:
        product *= cubes[color]
    return product


def is_game_possible(game):
    for i in range(1, game["total"] + 1):
        print("\t Checking Pull :", game[i])
        if not is_pull_valid(game[i]):
            print("Pull is not valid")
            return False
    print("Entire game is valid")
    return True


def main():
    print("Starting Script")
    running_sum = 0
    running_product_sum = 0
    parsed_content = parse_input_file("input.txt")
    split_content = parsed_content.split("\n")
    for line in split_content:
        if len(line) > 0:
            game_data = format_input_data(line)
            print("-- Current Running Sum: ", running_sum)
            print("\n Accessing New Game: ", game_data)
            if is_game_possible(game_data):
                running_sum += game_data["id"]
            minimum_cubes = find_minimum_amount_of_cubes(game_data)
            running_product_sum += get_product_of_cubes(minimum_cubes)
            print("Current Product Sum: ", running_product_sum)
    print(running_sum)


if __name__ == "__main__":
    main()
