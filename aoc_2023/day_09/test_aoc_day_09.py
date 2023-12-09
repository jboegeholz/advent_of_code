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
