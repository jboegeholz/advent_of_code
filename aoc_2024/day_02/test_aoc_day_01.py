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

def test_number_of_safe_reports():
    number_of_safe_reports = 0
    for line in data.split("\n"):
        safe_report = True
        values = line.split(" ")
        for i in range(len(values) - 1):
            if (int(values[i+1]) <= int(values[i]) or
               ((int(values[i+1]) - int(values[i]))) > 3):
                safe_report = False
                break

        if safe_report:
            number_of_safe_reports += 1

    assert number_of_safe_reports == 2

def test_number_of_safe_reports_full():
    number_of_safe_reports = 0
    safe_report = True
    with open("./aoc_data_01.txt", "r") as f:

        for line in f.readlines():
            values = line.rstrip().split(" ")
            for i in range(len(values) - 1):
                if abs(int(values[i]) - int(values[i+1])) > 3:
                    safe_report = False
                    break
            else:
                number_of_safe_reports += 1

    assert number_of_safe_reports == 2