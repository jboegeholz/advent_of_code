import pytest


"""
A for Rock, B for Paper, and C for Scissors
X for Rock, Y for Paper, and Z for Scissors
The score for a single round is the score for the shape you selected 
(1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round 
(0 if you lost, 3 if the round was a draw, and 6 if you won).
"""
data = """A Y
B X
C Z"""


def test_split_data():
    rounds = data.split("\n")
    assert rounds == ['A Y', 'B X', 'C Z']


strategy_dict = {
    'A X': 4,  # 1 + 3
    'A Y': 8,  # 2 + 6
    'A Z': 3,  # 3 + 0
    'B X': 1,  # 1 + 0
    'B Y': 5,  # 2 + 3
    'B Z': 9,  # 3 + 6
    'C X': 7,  # 1 + 6
    'C Y': 2,  # 2 + 0
    'C Z': 6,  # 3 + 3
}


def test_lookup_strategy_dict():
    score = 0
    rounds = data.split("\n")
    for round in rounds:
        score += strategy_dict[round]
    assert score == 15


def test_data_from_file_lookup_strategy_dict():
    with open("aoc_data_02.txt", "r") as f:
        data = f.read()

    score = 0
    rounds = data.split("\n")
    for round in rounds:
        score += strategy_dict[round]
    assert score == 11063
