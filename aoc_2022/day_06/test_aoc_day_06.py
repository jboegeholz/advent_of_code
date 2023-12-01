from collections import defaultdict

import pytest


@pytest.mark.parametrize(
    "data, expected",
    [
        ("mjqjpqm", 7),
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
        ("nppdvjthqldpwncqszvftbrmjlhg", 6),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11),
    ]
)
def test_marker(data, expected):
    marker_index = -1
    individual_chars = set()
    for i in range(4, len(data)):
        individual_chars.clear()
        individual_chars.add(data[i])
        individual_chars.add(data[i-1])
        individual_chars.add(data[i-2])
        individual_chars.add(data[i-3])
        if len(individual_chars) == 4:
            marker_index = i + 1
            break
    assert marker_index == expected


def test_marker_in_data():
    with open("aoc_data_06.txt", "r") as f:
        data = f.read()
    marker_index = -1
    individual_chars = set()
    for i in range(4, len(data)):
        individual_chars.clear()
        individual_chars.add(data[i])
        individual_chars.add(data[i-1])
        individual_chars.add(data[i-2])
        individual_chars.add(data[i-3])
        if len(individual_chars) == 4:
            marker_index = i + 1
            break
    assert marker_index == 1876

