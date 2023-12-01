from collections import defaultdict

import pytest


@pytest.mark.parametrize(
    "data, expected",
    [
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 23),
        ("nppdvjthqldpwncqszvftbrmjlhg", 23),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 26),
    ]
)
def test_marker(data, expected):
    marker_index = -1
    individual_chars = set()
    for i in range(14, len(data)):
        individual_chars.clear()
        for j in range(i, i-14, -1):
            individual_chars.add(data[j])
        if len(individual_chars) == 14:
            marker_index = i + 1
            break
    assert marker_index == expected


def test_marker_in_data():
    with open("aoc_data_06.txt", "r") as f:
        data = f.read()
    marker_index = -1
    individual_chars = set()
    for i in range(14, len(data)):
        individual_chars.clear()
        for j in range(i, i - 14, -1):
            individual_chars.add(data[j])
        if len(individual_chars) == 14:
            marker_index = i + 1
            break
    assert marker_index == 2202

