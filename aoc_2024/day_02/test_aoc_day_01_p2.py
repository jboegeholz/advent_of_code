from aoc_2024.day_02.test_aoc_day_01 import is_safe_report

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


def test_is_descending():
    data = "7 6 4 2 1"
    descending = True
    values = [int(x) for x in data.split(" ")]
    for i in range(len(values) - 1):
        if values[i+1] > values[i]:
            descending = False
    assert descending

def test_is_ascending():
    data = "1 3 6 7 9"
    ascending = True
    values = [int(x) for x in data.split(" ")]
    for i in range(len(values) - 1):
        if values[i+1] < values[i]:
            ascending = False
    assert ascending

def test_delta_between_one_and_three():
    data = "1 3 6 7 9"
    delta_ok = True
    values = [int(x) for x in data.split(" ")]
    for i in range(len(values) - 1):
        if not 1 <= abs(values[i+1] - values[i]) <=3:
            delta_ok = False
    assert delta_ok

def test_number_of_safe_reports():
    number_of_safe_reports = 0
    for line in data.split("\n"):
        values = [int(x) for x in line.rstrip().split(" ")]
        if is_safe_report(values):
            number_of_safe_reports += 1
        else:
            for i in range(len(values)):
                new_values = values.copy()
                new_values.pop(i)
                if is_safe_report(new_values):
                    number_of_safe_reports += 1
                    break


    assert number_of_safe_reports == 4

def test_number_of_safe_reports_full():
    number_of_safe_reports = 0

    with open("./aoc_data_01.txt", "r") as f:
        for line in f.readlines():
            values = [int(x) for x in line.rstrip().split(" ")]
            if is_safe_report(values):
                number_of_safe_reports += 1
            else:
                for i in range(len(values)):
                    new_values = values.copy()
                    new_values.pop(i)
                    if is_safe_report(new_values):
                        number_of_safe_reports += 1
                        break

    assert number_of_safe_reports == 2