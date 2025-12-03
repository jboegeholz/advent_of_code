from itertools import accumulate

import pytest

@pytest.mark.parametrize(
    "data, expected",
    [
        ("987654321111111", 98),
        ("811111111111119", 89),
        ("234234234234278", 78),
        ("818181911112111", 92)
    ]
)
def test_day_03_one_line_2(data, expected):
    line = data
    highest_joltage = 0
    second_highest_joltage = 0
    for j in range(len(line)):
        if j == len(line) - 1 and int(line[j]) > second_highest_joltage:
            second_highest_joltage = int(line[j])
            break
        i = int(line[j])
        if i > highest_joltage:
            highest_joltage = i
        if second_highest_joltage < i < highest_joltage:
            second_highest_joltage = i

    maximum_joltage = str(highest_joltage) + str(second_highest_joltage)
    assert int(maximum_joltage) == expected


def test_day_03_full_data():
    with open('data.txt', 'r', encoding='utf-8') as f:
        data = f.readlines()
    accumulated_joltage = 0
    for line in data:
        line = line.strip()
        highest_joltage = 0
        second_highest_joltage = 0
        for j in range(len(line)):
            if j == len(line) - 1 and int(line[j]) > second_highest_joltage:
                second_highest_joltage = int(line[j])
                break
            i = int(line[j])
            if i > highest_joltage:
                highest_joltage = i
            if second_highest_joltage < i < highest_joltage:
                second_highest_joltage = i

        maximum_joltage = str(highest_joltage) + str(second_highest_joltage)
        accumulated_joltage += int(maximum_joltage)

    assert accumulated_joltage == 17416

