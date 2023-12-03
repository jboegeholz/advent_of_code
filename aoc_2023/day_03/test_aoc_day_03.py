data="""467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

symbols = "*+#$"

test_data = """...
.1.
..."""

test_data_2 = """....
.12..
...."""

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