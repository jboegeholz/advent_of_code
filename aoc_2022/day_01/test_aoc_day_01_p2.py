calories = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""


def test_calc_overall_max_calories():
    calories_inventory = []
    list_all_cal = calories.split("\n\n")
    for i, list_cal in enumerate(list_all_cal):
        list_individual_cal = [int(x) for x in list_cal.split("\n")]
        sum_cal = sum(list_individual_cal)
        calories_inventory.append((sum_cal, i))

    calories_inventory.sort(reverse=True)
    assert calories_inventory[0] == (24000, 3)
    assert calories_inventory[1] == (11000, 2)
    assert calories_inventory[2] == (10000, 4)


def test_calc_overall_max_calories_from_file():
    with open("aoc_data_01.txt", "r") as f:
        data = f.read()

    calories_inventory = []
    list_all_cal = data.split("\n\n")
    for i, list_cal in enumerate(list_all_cal):
        list_individual_cal = [int(x) for x in list_cal.split("\n")]
        sum_cal = sum(list_individual_cal)
        calories_inventory.append((sum_cal, i))

    calories_inventory.sort(reverse=True)

    assert calories_inventory[0] == (67027, 12)
    assert calories_inventory[1] == (65333, 27)
    assert calories_inventory[2] == (64931, 234)

    assert calories_inventory[0][0] + calories_inventory[1][0] + calories_inventory[2][0] == 197291

