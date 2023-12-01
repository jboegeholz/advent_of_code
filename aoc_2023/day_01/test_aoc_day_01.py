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
    calibration_value_str = ""
    for c in line:
        if c.isdigit():
            calibration_value_str += c
            break
    for c in line[::-1]:
        if c.isdigit():
            calibration_value_str += c
            break
    assert calibration_value_str == "77"
