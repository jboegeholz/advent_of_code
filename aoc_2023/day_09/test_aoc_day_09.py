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

    differences_2.append(0)
    assert differences_2 == [0, 0, 0, 0, 0]

    differences.append(differences_2[-1] + differences[-1])
    assert differences == [3, 3, 3, 3, 3, 3]

    next_value = differences[-1] + line[-1]
    assert next_value == 18


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

    differences_2.append(differences_3[-1] + differences_2[-1])
    assert differences_2 == [1, 1, 1, 1, 1]

    differences.append(differences[-1] + differences_2[-1])

    assert differences == [2,   3,   4,   5,   6,   7]
    next_value = differences[-1] + line[-1]
    assert next_value == 28