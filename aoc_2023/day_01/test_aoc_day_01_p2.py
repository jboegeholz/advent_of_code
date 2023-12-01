import pytest

data = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""
numbers_as_words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
numbers_as_words_reversed = ["orez", "eno", "owt", "eerht", "ruof", "evif", "xis", "neves", "thgie", "enin"]


def test_first_digit_or_naw():
    calibration_value_str = ""
    line = "4nine"
    first_digit = ""
    first_digit_pos = -1
    first_naw = ""
    first_naw_pos = -1
    for i, c in enumerate(line):
        if c.isdigit():
            first_digit += c
            first_digit_pos = i
            break
    for niw in numbers_as_words:
        if niw in line:
            first_naw = str(numbers_as_words.index(niw))
            first_naw_pos = line.find(niw)
            break
    if first_digit_pos < first_naw_pos:
        calibration_value_str = first_digit
    else:
        calibration_value_str = first_naw
    calibration_value = int(calibration_value_str)
    assert 4 == calibration_value


def test_last_digit_or_naw():
    calibration_value_str = ""
    line = "4nine"[::-1]
    last_digit = ""
    last_digit_pos = -1
    last_naw = ""
    last_naw_pos = -1
    for i, c in enumerate(line):
        if c.isdigit():
            last_digit += c
            last_digit_pos = i
            break
    for niw in numbers_as_words_reversed:
        if niw in line:
            last_naw = str(numbers_as_words_reversed.index(niw))
            last_naw_pos = line.find(niw)

    if last_digit_pos < last_naw_pos:
        calibration_value_str += last_digit
    else:
        calibration_value_str += last_naw
    calibration_value = int(calibration_value_str)
    assert 9 == calibration_value

def test_day_2():
    line = "two1nine"
    calibration_value_str = ""
    calibration_value_str += get_first_digit(line)
    calibration_value_str += get_last_digit(line[::-1])
    calibration_value = int(calibration_value_str)
    assert 29 == calibration_value

@pytest.mark.parametrize(
    "data, expected",
    [
        ("two1nine", 29),
        ("eightwothree", 83),
        ("abcone2threexyz", 13),
        ("xtwone3four", 24),
        ("4nineeightseven2", 42),
        ("zoneight234", 14),
        ("7pqrstsixteen", 76),
    ]
)
def test_first_last_digit(data, expected):
    line = data
    calibration_value_str = ""
    calibration_value_str += get_first_digit(line)
    line = line[::-1]
    calibration_value_str += get_last_digit(line)
    calibration_value = int(calibration_value_str)
    assert calibration_value == expected

def get_first_digit(line):
    first_digit = ""
    first_digit_pos = -1
    first_naw = ""
    first_naw_pos = 1000
    for i, c in enumerate(line):
        if c.isdigit():
            first_digit += c
            first_digit_pos = i
            break
    for niw in numbers_as_words:
        if niw in line:
            current_naw_pos = line.find(niw)
            if current_naw_pos < first_naw_pos:
                first_naw_pos = current_naw_pos
                first_naw = str(numbers_as_words.index(niw))

    if first_digit_pos != -1 and first_digit_pos < first_naw_pos:
        return first_digit
    else:
        return first_naw

def get_last_digit(line):
    last_digit = ""
    last_digit_pos = 1000
    last_naw = ""
    last_naw_pos = 1000
    for i, c in enumerate(line):
        if c.isdigit():
            last_digit += c
            last_digit_pos = i
            break
    for niw in numbers_as_words_reversed:
        if niw in line:
            current_naw_pos = line.find(niw)
            if current_naw_pos < last_naw_pos:
                last_naw_pos = current_naw_pos
                last_naw = str(numbers_as_words_reversed.index(niw))

    if last_digit_pos < last_naw_pos:
        return last_digit
    else:
        return last_naw





def test_calculate_calibration_values():
    with open("aoc_data_01.txt", "r") as f:
        data = f.read()
    calibration_values = 0
    for line in data.split("\n"):
        calibration_value_str = ""
        calibration_value_str += get_first_digit(line)

        line = line[::-1]

        calibration_value_str += get_last_digit(line)

        calibration_values += int(calibration_value_str)

    assert 55260 == calibration_values
