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

def test_calc_similarity_score():
    similarity_score = 0
    list_1 = []
    list_2 = []
    for line in data.split("\n"):
        list_1.append(int(line.split("   ")[0]))
        list_2.append(int(line.split("   ")[1]))

    for item_1 in list_1:
        sim_counter = 0
        for item_2 in list_2:
            if item_1 == item_2:
                sim_counter += 1
        similarity_score += sim_counter * item_1
    assert similarity_score == 31

def test_calc_similarity_score_full():
    similarity_score = 0
    list_1 = []
    list_2 = []
    with open("./aoc_data_01.txt", "r") as f:
        for line in f.readlines():
            line = line.rstrip('\r*\n')
            list_1.append(int(line.split("   ")[0]))
            list_2.append(int(line.split("   ")[1]))

    for item_1 in list_1:
        sim_counter = 0
        for item_2 in list_2:
            if item_1 == item_2:
                sim_counter += 1
        similarity_score += sim_counter * item_1
    assert similarity_score == 31

