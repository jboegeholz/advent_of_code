data = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""
def test_next_value():
    line = [int(c) for c in "0 3 6 9 12 15".split(" ")]
    differences = []
    for i in range(len(line)-1):
        differences.append(line[i+1] - line[i])
    assert differences == [3, 3, 3, 3, 3]

    differences_2 = []
    for i in range(len(differences)-1):
        differences_2.append(differences[i+1] - differences[i])
    assert differences_2 == [0, 0, 0, 0]

    differences_2.insert(0, 0)
    assert differences_2 == [0, 0, 0, 0, 0]

    differences.insert(0, differences_2[0] + differences[0])
    assert differences == [3, 3, 3, 3, 3, 3]

    next_value = differences[0] + line[0]
    assert next_value == 3


def all_zero(differences):
    is_zero = True
    for d in differences:
        if d != 0:
            is_zero = False
    return is_zero


def test_next_value_2():
    line = [int(c) for c in "1 3 6 10 15 21".split(" ")]
    differences = []
    for i in range(len(line)-1):
        differences.append(line[i+1] - line[i])
    assert differences == [2, 3, 4, 5, 6]

    differences_2 = []
    for i in range(len(differences)-1):
        differences_2.append(differences[i+1] - differences[i])
    assert differences_2 == [1, 1, 1, 1]

    differences_3 = []
    for i in range(len(differences_2)-1):
        differences_3.append(differences_2[i+1] - differences_2[i])
    assert differences_3 == [0, 0, 0]

    differences_3.append(0)
    assert all_zero(differences_3)
    assert differences_3 == [0, 0, 0, 0]

    differences_2.insert(0, (differences_3[0] + differences_2[0]))
    assert differences_2 == [1, 1, 1, 1, 1]

    differences.insert(0, (differences[0] + differences_2[0]))

    assert differences == [3, 2, 3, 4, 5, 6]
    next_value = differences[0] + line[0]
    assert next_value == 4


def test_next_value_3():
    line = [int(c) for c in "10 13 16 21 30 45".split(" ")]
    all_differences = []
    all_differences.append(line)
    # generate differences
    while not all_zero(all_differences[-1]):
        current_diff = all_differences[-1]
        differences = []
        for i in range(len(current_diff) - 1):
            differences.append(current_diff[i + 1] - current_diff[i])
        all_differences.append(differences)

    assert all_differences == [[10, 13, 16, 21, 30, 45], [3, 3, 5, 9, 15], [0, 2, 4, 6], [2, 2, 2], [0, 0]]

    all_differences[-1].insert(0, 0)

    assert all_differences == [[10, 13, 16, 21, 30, 45], [3, 3, 5, 9, 15], [0, 2, 4, 6], [2, 2, 2], [0, 0, 0]]

    for i in range(len(all_differences)-1, 0, -1):
        current_diff = all_differences[i]
        all_differences[i-1].insert(0, (all_differences[i-1][0] - current_diff[0] ))

    assert all_differences == [[5, 10, 13, 16, 21, 30, 45], [5, 3, 3, 5, 9, 15], [-2, 0, 2, 4, 6], [2, 2, 2, 2], [0, 0, 0]]

    next_value = all_differences[0][0]
    assert next_value == 5

def test_next_value_with_data():
    with open("aoc_data_09.txt", "r") as f:
        real_data = f.read()
    lines = real_data.split("\n")
    sum_of_extrapolated_values = 0
    for line in lines:
        line = [int(c) for c in line.split(" ")]
        all_differences = []
        all_differences.append(line)
        # generate differences
        while not all_zero(all_differences[-1]):
            current_diff = all_differences[-1]
            differences = []
            for i in range(len(current_diff) - 1):
                differences.append(current_diff[i + 1] - current_diff[i])
            all_differences.append(differences)

        all_differences[-1].insert(0, 0)

        for i in range(len(all_differences)-1, 0, -1):
            current_diff = all_differences[i]
            all_differences[i - 1].insert(0, (all_differences[i - 1][0] - current_diff[0]))

        next_value = all_differences[0][0]
        sum_of_extrapolated_values += next_value
    assert sum_of_extrapolated_values == 1053