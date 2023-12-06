import pytest

from day_2.day_2 import (
    format_input_data,
    is_game_possible,
    is_pull_valid,
    validate_game,
)


class TestDay2:
    def test_validate_game(self):
        assert validate_game(
            "Game 1: 2 blue, 3 red; 3 green, 3 blue, 6 red; 4 blue, 6 red; 2 green, 2 blue, 9 red; 2 red, 4 blue"
        ) == {"id": 1, "blue": 15, "red": 26, "green": 5}
        assert validate_game(
            "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue"
        ) == {"id": 2, "blue": 6, "red": 1, "green": 6}
        assert validate_game(
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"
        ) == {"id": 3, "blue": 11, "red": 25, "green": 26}
        assert validate_game(
            "Game 100: 7 blue, 9 green, 2 red; 5 red, 9 green; 1 blue, 8 red, 13 green"
        ) == {"id": 100, "blue": 8, "red": 15, "green": 31}
        assert validate_game(
            "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
        ) == {"id": 5, "blue": 3, "red": 7, "green": 5}

    def test_format_input_data(self):
        assert format_input_data(
            "Game 1: 2 blue, 3 red; 3 green, 3 blue, 6 red; 4 blue, 6 red; 2 green, 2 blue, 9 red; 2 red, 4 blue"
        ) == {
            "id": 1,
            "total": 5,
            1: {"blue": 2, "red": 3, "green": 0},
            2: {"blue": 3, "red": 6, "green": 3},
            3: {"blue": 4, "red": 6, "green": 0},
            4: {"blue": 2, "red": 9, "green": 2},
            5: {"blue": 4, "red": 2, "green": 0},
        }
        assert format_input_data(
            "Game 100: 7 blue, 9 green, 2 red; 5 red, 9 green; 1 blue, 8 red, 13 green"
        ) == {
            "id": 100,
            "total": 3,
            1: {"blue": 7, "red": 2, "green": 9},
            2: {"blue": 0, "red": 5, "green": 9},
            3: {"blue": 1, "red": 8, "green": 13},
        }

    def test_is_pull_valid(self):
        assert (
            is_pull_valid({"id": 1, "blue": 15, "red": 26, "green": 5})
            == False
        )
        assert (
            is_pull_valid({"id": 2, "blue": 6, "red": 1, "green": 6}) == True
        )
        assert (
            is_pull_valid({"id": 3, "blue": 11, "red": 25, "green": 26})
            == False
        )
        assert (
            is_pull_valid({"id": 100, "blue": 8, "red": 15, "green": 31})
            == False
        )
        assert (
            is_pull_valid({"id": 5, "blue": 3, "red": 7, "green": 5}) == True
        )

    def test_is_game_possible(self):
        assert (
            is_game_possible(
                {
                    "id": 98,
                    "total": 5,
                    1: {"blue": 2, "red": 6, "green": 3},
                    2: {"blue": 1, "red": 8, "green": 1},
                    3: {"blue": 1, "red": 8, "green": 3},
                    4: {"blue": 2, "red": 0, "green": 0},
                    5: {"blue": 2, "red": 8, "green": 2},
                }
            )
            == True
        )
        assert (
            is_game_possible(
                {
                    "id": 74,
                    "total": 5,
                    1: {"blue": 3, "red": 7, "green": 0},
                    2: {"blue": 3, "red": 2, "green": 5},
                    3: {"blue": 3, "red": 5, "green": 1},
                    4: {"blue": 2, "red": 11, "green": 8},
                    5: {"blue": 3, "red": 10, "green": 8},
                }
            )
            == True
        )
        assert (
            is_game_possible(
                {
                    "id": 53,
                    "total": 6,
                    1: {"blue": 2, "red": 1, "green": 4},
                    2: {"blue": 8, "red": 4, "green": 7},
                    3: {"blue": 7, "red": 14, "green": 6},
                    4: {"blue": 1, "red": 3, "green": 7},
                    5: {"blue": 9, "red": 2, "green": 5},
                    6: {"blue": 10, "red": 7, "green": 1},
                }
            )
            == False
        )
        assert (
            is_game_possible(
                {
                    "id": 40,
                    "total": 6,
                    1: {"blue": 4, "red": 0, "green": 8},
                    2: {"blue": 5, "red": 7, "green": 8},
                    3: {"blue": 5, "red": 0, "green": 8},
                    4: {"blue": 21, "red": 3, "green": 6},
                    5: {"blue": 14, "red": 2, "green": 7},
                    6: {"blue": 5, "red": 7, "green": 1},
                }
            )
            == False
        )
