data = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

test_data = """...
.1.
..."""


def test_convert_to_2d_array():
    # convert data to 2d array
    data_array = []
    for line in test_data.splitlines():
        line_array = []
        for j, c in enumerate(line):
            line_array.append(c)
        data_array.append(line_array)

    assert data_array == [[".", ".", "."], [".", "1", "."], [".", ".", "."]]


def test_find_single_digit_number():
    part_number = 0
    data_array = []
    for line in test_data.splitlines():
        line_array = []
        for j, c in enumerate(line):
            line_array.append(c)
        data_array.append(line_array)

    for i, row in enumerate(data_array):
        for j, c in enumerate(row):
            if c.isdigit():
                part_number = c

    assert part_number == "1"


test_data_2 = """....
.12..
...."""


def test_find_two_digit_number():
    part_number = ""
    data_array = []
    for line in test_data_2.splitlines():
        line_array = []
        for j, c in enumerate(line):
            line_array.append(c)
        data_array.append(line_array)

    for i, row in enumerate(data_array):
        for j, c in enumerate(row):
            if c.isdigit():
                part_number += c

    assert part_number == "12"


test_data_3 = """.....
.123..
.234.
....."""


def test_find_two_part_numbers():
    part_numbers = []
    data_array = []
    for line in test_data_3.splitlines():
        line_array = []
        for j, c in enumerate(line):
            line_array.append(c)
        data_array.append(line_array)

    for i, row in enumerate(data_array):
        part_number = ""
        for j, c in enumerate(row):
            if c.isdigit():
                part_number += c
            else:
                if part_number:
                    part_numbers.append(part_number)
                    part_number = ""
    assert part_numbers == ['123', '234']


test_data_4 = """.......
........
..123...
........
........"""


def test_is_part_number():
    part_numbers = []
    data_array = []
    for line in test_data_4.splitlines():
        line_array = []
        for j, c in enumerate(line):
            line_array.append(c)
        data_array.append(line_array)

    for i in range(0, len(data_array)-1):
        part_number = ""
        for j in range(0, len(data_array[i]) - 1):
            if data_array[i][j].isdigit():
                part_number += data_array[i][j]
            else:
                if part_number:
                    part_number_length = len(part_number)
                    is_part_number = False
                    if part_number_length == 1:
                        # search perimeter 8
                        if data_array[i - 1][j - 2] != '.':
                            is_part_number = True
                        if data_array[i - 1][j - 1] != '.':
                            is_part_number = True
                        if data_array[i - 1][j] != '.':
                            is_part_number = True
                        if data_array[i][j - 2] != '.':
                            is_part_number = True
                        if data_array[i][j] != '.':
                            is_part_number = True
                        if data_array[i + 1][j - 2] != '.':
                            is_part_number = True
                        if data_array[i + 1][j - 1] != '.':
                            is_part_number = True
                        if data_array[i + 1][j] != '.':
                            is_part_number = True
                    if part_number_length == 2:
                        if data_array[i - 1][j - 2] != '.':
                            is_part_number = True
                        if data_array[i - 1][j - 1] != '.':
                            is_part_number = True
                        if data_array[i - 1][j] != '.':
                            is_part_number = True
                        if data_array[i][j - 2] != '.':
                            is_part_number = True
                        if data_array[i][j] != '.':
                            is_part_number = True
                        if data_array[i + 1][j - 2] != '.':
                            is_part_number = True
                        if data_array[i + 1][j - 1] != '.':
                            is_part_number = True
                        if data_array[i + 1][j] != '.':
                            is_part_number = True
                        # search perimeter 10
                        if data_array[i-1][j - 3] != '.':
                            is_part_number = True
                        if data_array[i][j - 3] != '.':
                            is_part_number = True
                        if data_array[i+1][j - 3] != '.':
                            is_part_number = True
                    if part_number_length == 3:
                        if data_array[i - 1][j - 2] != '.':
                            is_part_number = True
                        if data_array[i - 1][j - 1] != '.':
                            is_part_number = True
                        if data_array[i - 1][j] != '.':
                            is_part_number = True
                        if data_array[i][j - 2] != '.':
                            is_part_number = True
                        if data_array[i][j] != '.':
                            is_part_number = True
                        if data_array[i + 1][j - 2] != '.':
                            is_part_number = True
                        if data_array[i + 1][j - 1] != '.':
                            is_part_number = True
                        if data_array[i + 1][j] != '.':
                            is_part_number = True
                            # search perimeter 10
                        if data_array[i - 1][j - 4] != '.':
                            is_part_number = True
                        if data_array[i][j - 4] != '.':
                            is_part_number = True
                        if data_array[i + 1][j - 4] != '.':
                            is_part_number = True
                        # search perimeter 12
                        if data_array[i-1][j - 3] != '.':
                            is_part_number = True
                        if data_array[i][j - 3] != '.':
                            is_part_number = True
                        if data_array[i+1][j - 3] != '.':
                            is_part_number = True
                    if is_part_number:
                        part_numbers.append(part_number)
                        part_number = ""

    assert part_numbers == ["123"]

def test_sum_partnumbers():
    pass

