import re
import pytest

@pytest.mark.parametrize(
    "data, expected",
    [
        ("don't()xyzdon't()xyzdo()abc", "do()abc"),
        ("don't()xyzdo()abcdon't()xyz", "do()abc"),
        ("do()abcdon't()xyzdo()abc", "do()abcdo()abc"),
        ("do()abcdo()abcdon't()xyz", "do()abcdo()abc"),
        ("abcdo()abcdon't()xyzdo()abc", "abcdo()abcdo()abc"),
        ("xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))", "xmul(2,4)&mul[3,7]!^do()?mul(8,5))"),
    ]
)
def test_fully_split(data, expected):
    data = re.sub(r"don't\(\).+(?=do\(\))", '', data)
    data = re.sub(r"don't\(\).+", '', data)

    assert data == expected


def test_regex_full_data_multiply():
    # sanitize data
    # add newline before every do and don't
    # delete every don't line
    # delete newlines
    with (open("aoc_data_03.txt", "r") as f):
        data = f.read()
        data = re.sub(r"\s", '', data)
        sum_of_products = 0
        p = re.compile(r"mul\(\d+,\d+\)")
        result = p.findall(data)
        for instruction in result:
            splitted = instruction.split("mul(")
            numbers = splitted[1].rstrip(")").split(",")
            product = int(numbers[0]) * int(numbers[1])
            sum_of_products += product

        assert sum_of_products == 53783319
        # too low   32753109
        # not right 36130721
        # too high  69631176