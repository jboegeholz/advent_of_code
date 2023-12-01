import string

data = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""


def test_split_rucksacks():
    first_rucksack = data.split("\n")[0]
    assert first_rucksack == "vJrwpWtwJgWrhcsFMMfFFhFp"


def test_split_rucksack_items():
    first_rucksack = data.split("\n")[0]
    split_point = len(first_rucksack) // 2
    first_rucksack_item = first_rucksack[0:split_point]
    assert first_rucksack_item == "vJrwpWtwJgWr"

    second_rucksack_item = first_rucksack[split_point:]
    assert second_rucksack_item == "hcsFMMfFFhFp"


def test_check_common_char():
    first_rucksack_item = "vJrwpWtwJgWr"
    second_rucksack_item = "hcsFMMfFFhFp"
    a = list(set(first_rucksack_item) & set(second_rucksack_item))
    assert a == ['p']


def test_lookup_char_value():
    chars = string.ascii_letters
    value = chars.index('p') + 1
    assert value == 16

    value = chars.index('L') + 1
    assert value == 38


def test_sum_priorities():
    sum_of_list = 0
    chars = string.ascii_letters
    rucksacks = data.split("\n")
    for rucksack in rucksacks:
        split_point = len(rucksack) // 2
        first_rucksack_item = rucksack[0:split_point]
        second_rucksack_item = rucksack[split_point:]
        common_char = list(set(first_rucksack_item) & set(second_rucksack_item))
        value = chars.index(common_char[0]) + 1
        sum_of_list += value

    assert sum_of_list == 157


def test_sum_priorities_data():
    with open("aoc_data_03.txt", "r") as f:
        data_from_file = f.read()
    sum_of_list = 0
    chars = string.ascii_letters
    rucksacks = data_from_file.split("\n")
    for rucksack in rucksacks:
        split_point = len(rucksack) // 2
        first_rucksack_item = rucksack[0:split_point]
        second_rucksack_item = rucksack[split_point:]
        common_char = list(set(first_rucksack_item) & set(second_rucksack_item))
        value = chars.index(common_char[0]) + 1
        sum_of_list += value

    assert sum_of_list == 8202
