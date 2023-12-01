import string

data="""vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""


def test_split_rucksacks():
    first_rucksack = data.split("\n")[0]
    assert first_rucksack == "vJrwpWtwJgWrhcsFMMfFFhFp"


def test_find_badge():
    rucksacks = data.split("\n")
    common_char = list(set(rucksacks[0]) & set(rucksacks[1]) & set(rucksacks[2]))
    assert common_char == ['r']


def test_find_badges():
    rucksacks = data.split("\n")
    common_chars = []
    for i in range(0, len(rucksacks), 3):
        common_char = list(set(rucksacks[i]) & set(rucksacks[i+1]) & set(rucksacks[i+2]))
        common_chars.append(common_char)

    assert common_chars[0] == ['r']
    assert common_chars[1] == ['Z']


def test_calculate_sum_of_badges():
    rucksacks = data.split("\n")
    chars = string.ascii_letters
    sum_of_badges = 0
    for i in range(0, len(rucksacks), 3):
        common_char = list(set(rucksacks[i]) & set(rucksacks[i+1]) & set(rucksacks[i+2]))
        sum_of_badges += chars.index(common_char[0]) + 1

    assert sum_of_badges == 70

def test_calculate_sum_of_badges_data():
    with open("aoc_data_03.txt", "r") as f:
        data_from_file = f.read()
    rucksacks = data_from_file.split("\n")
    chars = string.ascii_letters
    sum_of_badges = 0
    for i in range(0, len(rucksacks), 3):
        common_char = list(set(rucksacks[i]) & set(rucksacks[i+1]) & set(rucksacks[i+2]))
        sum_of_badges += chars.index(common_char[0]) + 1

    assert sum_of_badges == 2864