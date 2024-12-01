data = """3   4
4   3
2   5
1   3
3   9
3   3"""
def test_convert_to_lists():
    list_1 = []
    list_2 = []
    for line in data.split("\n"):
        list_1.append(line.split("   ")[0])
        list_2.append(line.split("   ")[1])

    assert list_1 != []
    assert list_2 != []

def test_count_distance():
    total_distance = 0
    list_1 = []
    list_2 = []
    for line in data.split("\n"):
        list_1.append(int(line.split("   ")[0]))
        list_2.append(int(line.split("   ")[1]))
    list_1.sort()
    list_2.sort()
    for i, item in enumerate(list_1):
        distance = abs(list_1[i] - list_2[i])
        total_distance += distance

    assert 11 == total_distance

def test_solve_puzzele():
    total_distance = 0
    list_1 = []
    list_2 = []
    with open("./aoc_data_01.txt", "r") as f:
        for line in f.readlines():
            line = line.rstrip('\r*\n')
            list_1.append(int(line.split("   ")[0]))
            list_2.append(int(line.split("   ")[1]))


    list_1.sort()
    list_2.sort()
    for i, item in enumerate(list_1):
        distance = abs(list_1[i] - list_2[i])
        total_distance += distance
    assert 11 == total_distance