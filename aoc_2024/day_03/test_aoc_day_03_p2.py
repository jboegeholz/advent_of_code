from aoc_2024.day_02.test_aoc_day_02 import is_safe_report

data = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""
def test_convert_to_lists():

    for line in data.split("\n"):
        print(line)

    assert line == '1 3 6 7 9'
