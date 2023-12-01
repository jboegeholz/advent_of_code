import pytest

"""
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 
"""
test_stacks = [
    ["Z", "N"],
    ["M", "C", "D"],
    ["P"]
]

test_moves = """move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""


def test_split_move():
    move_input = "move 1 from 2 to 1"
    move = [int(x) for x in move_input.split(" ") if x.isdigit()]
    assert move == [1, 2, 1]


def test_move_container():
    move_input = "move 1 from 2 to 1"
    move = [int(x) for x in move_input.split(" ") if x.isdigit()]
    amount = move[0]
    src = move[1] - 1
    dst = move[2] - 1
    for i in range(amount):
        item = test_stacks[src].pop()
        test_stacks[dst].append(item)
    end = [
        ["Z", "N", "D"],
        ["M", "C"],
        ["P"]
    ]
    assert test_stacks == end


def test_move_all_container():
    for move_input in test_moves.split("\n"):
        move = [int(x) for x in move_input.split(" ") if x.isdigit()]
        amount = move[0]
        src = move[1] - 1
        dst = move[2] - 1
        for i in range(amount):
            item = test_stacks[src].pop()
            test_stacks[dst].append(item)
    end = [
        ["C"],
        ["M"],
        ["P", "D", "N", "Z"]
    ]
    assert test_stacks == end


"""
        [M]     [B]             [N]
[T]     [H]     [V] [Q]         [H]
[Q]     [N]     [H] [W] [T]     [Q]
[V]     [P] [F] [Q] [P] [C]     [R]
[C]     [D] [T] [N] [N] [L] [S] [J]
[D] [V] [W] [R] [M] [G] [R] [N] [D]
[S] [F] [Q] [Q] [F] [F] [F] [Z] [S]
[N] [M] [F] [D] [R] [C] [W] [T] [M]
 1   2   3   4   5   6   7   8   9


"""

stacks = [
    ["N", "S", "D", "C", "V", "Q", "T"],
    ["M", "F", "V"],
    ["F", "Q", "W", "D", "P", "N", "H", "M"],
    ["D", "Q", "R", "T", "F"],
    ["R", "F", "M", "N", "Q", "H", "V", "B"],
    ["C", "F", "G", "N", "P", "W", "Q"],
    ["W", "F", "R", "L", "C", "T"],
    ["T", "Z", "N", "S"],
    ["M", "S", "D", "J", "R", "Q", "H", "N"],
]


def test_move_all_container_from_file():
    with open("aoc_data_05.txt", "r") as f:
        moves = f.read()
    for move_input in moves.split("\n"):
        move = [int(x) for x in move_input.split(" ") if x.isdigit()]
        amount = move[0]
        src = move[1] - 1
        dst = move[2] - 1
        for i in range(amount):
            item = stacks[src].pop()
            stacks[dst].append(item)

    top_crates = ""
    for stack in stacks:
        top_crates += stack.pop()
    assert top_crates == "FRDSQRRCD"
