import re
import pytest

@pytest.mark.parametrize(
    "data, expected",
    [
        ("don't()xyzdon't()xyzdo()abc", "do()abc"),
    ]
)
def test_fully_split(data, expected):
    data = re.sub(r"don't\(\).+(?=do\(\))", '', data)

    assert data == expected


def test_regex_full_data_multiply():
    with (open("aoc_data_03.txt", "r") as f):
        data = f.read()
        data = re.sub(r"don't\(\).+(?=do\(\))", '', data)
        data = re.sub(r"don't\(\).+(?=don't\(\))", '', data)
        sum_of_products = 0
        p = re.compile(r"mul\(\d+,\d+\)")
        result = p.findall(data)
        for instruction in result:
            splitted = instruction.split("mul(")
            numbers = splitted[1].rstrip(")").split(",")
            product = int(numbers[0]) * int(numbers[1])
            sum_of_products += product

        assert sum_of_products == 36130721
        # too low   32753109
        # not right 36130721
        # too high  69631176