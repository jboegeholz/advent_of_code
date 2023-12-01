import pytest


@pytest.mark.parametrize(
    "move, starting_position_head, starting_position_tail, position_head_expected, position_tail_expected",
    [
        ("R 1", [0, 0], [0, 0], [1, 0], [0, 0]),
        ("U 1", [0, 0], [0, 0], [0, 1], [0, 0]),
        ("D 1", [0, 1], [0, 0], [0, 0], [0, 0]),
        ("L 1", [1, 0], [0, 0], [0, 0], [0, 0]),
        ("R 2", [0, 0], [0, 0], [2, 0], [1, 0]),
        ("R 3", [0, 0], [0, 0], [3, 0], [2, 0]),
        ("U 2", [1, 0], [0, 0], [1, 2], [1, 1]),
        ("R 2", [0, 1], [0, 0], [2, 1], [1, 1]),
    ]
)
def test_convert_move(move, starting_position_head, starting_position_tail, position_head_expected, position_tail_expected):
    position_head = starting_position_head
    position_tail = starting_position_tail
    if "R" in move:
        amount = int(move.split(" ")[1])
        for i in range(amount):
            position_head[0] += 1
            if position_tail[0] + 2 <= position_head[0]:
                position_tail[0] += 1
                position_tail[1] = position_head[1]
    if "U" in move:
        amount = int(move.split(" ")[1])
        for i in range(amount):
            position_head[1] += 1
            if position_tail[1] + 2 <= position_head[1]:
                position_tail[1] += 1
                position_tail[0] = position_head[0]
    if "D" in move:
        amount = int(move.split(" ")[1])
        position_head[1] -= amount
    if "L" in move:
        amount = int(move.split(" ")[1])
        position_head[0] -= amount
    assert position_head == position_head_expected
    assert position_tail == position_tail_expected
