data = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

def test_stuff():
    line = "1abc2"
    calibration_value = int(line[0] + line[-1])
    assert 12 == calibration_value


def test_second_line():
    line = "pqr3stu8vwx"
    calibration_value_str = ""
    for c in line:
        if c.isdigit():
            calibration_value_str += c
    assert calibration_value_str == "38"

def test_third_line():
    line = "a1b2c3d4e5f"
    calibration_value_str = ""
    for c in line:
        if c.isdigit():
            calibration_value_str += c
            break
    for c in line[::-1]:
        if c.isdigit():
            calibration_value_str += c
            break
    assert calibration_value_str == "15"

def test_fourth_line():
    line = "treb7uchet"
    calibration_value_str = get_calibration_string(line)
    assert calibration_value_str == "77"

def test_with_test_data():
    sum_of_calibration_value = 0
    for line in data.split("\n"):
        sum_of_calibration_value += int(get_calibration_string(line))

    assert sum_of_calibration_value == 142

def test_with_real_data():
    with open("aoc_data_01.txt", "r") as f:
        data = f.read()
    sum_of_calibration_value = 0
    for line in data.split("\n"):
        sum_of_calibration_value += int(get_calibration_string(line))

    assert sum_of_calibration_value == 55123
def get_calibration_string(line):
    calibration_value_str = ""
    for c in line:
        if c.isdigit():
            calibration_value_str += c
            break
    for c in line[::-1]:
        if c.isdigit():
            calibration_value_str += c
            break
    return calibration_value_str
