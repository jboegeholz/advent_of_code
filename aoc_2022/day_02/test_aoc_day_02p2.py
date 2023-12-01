import pytest


"""
A for Rock, B for Paper, and C for Scissors

X lose
Y draw
Z win
"""
data = """A Y
B X
C Z"""


def test_split_data():
    rounds = data.split("\n")
    assert rounds == ['A Y', 'B X', 'C Z']



strategy_dict = {
    'A X': 3,  # 3 + 0
    'A Y': 4,  # 1 + 3
    'A Z': 8,  # 2 + 6
    'B X': 1,  # 1 + 0
    'B Y': 5,  # 2 + 3
    'B Z': 9,  # 3 + 6
    'C X': 2,  # 2 + 0
    'C Y': 6,  # 3 + 3
    'C Z': 7,  # 1 + 6
}


def test_lookup_strategy_dict():
    score = 0
    rounds = data.split("\n")
    for round in rounds:
        score += strategy_dict[round]
    assert score == 12


def test_data_from_file_lookup_strategy_dict():
    with open("aoc_data_02.txt", "r") as f:
        data = f.read()

    score = 0
    rounds = data.split("\n")
    for round in rounds:
        score += strategy_dict[round]
    assert score == 10349
