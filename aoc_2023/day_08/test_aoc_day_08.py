import pytest

data = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""


def test_get_steps():
    steps = list(data.split("\n\n")[0])

    assert steps == ['L', 'L', 'R']


def test_get_map():
    map = create_map(data)
    assert map == {
        'AAA': ['BBB', 'BBB'],
        'BBB': ['AAA', 'ZZZ'],
        'ZZZ': ['ZZZ', 'ZZZ']
    }


def create_map(data):
    map = []
    raw_map = data.split("\n\n")[1].split("\n")
    for map_item in raw_map:
        cur_loc = map_item.split(" = ")[0]
        possible_dest = map_item.split(" = ")[1].replace("(", "")
        possible_dest_l = possible_dest.split(", ")[0].replace("(", "")
        possible_dest_r = possible_dest.split(", ")[1].replace(")", "")
        map.append([cur_loc, [possible_dest_l, possible_dest_r]])
    return map


def test_walk():
    steps = list(data.split("\n\n")[0])
    map = {}
    raw_map = data.split("\n\n")[1].split("\n")
    for map_item in raw_map:
        cur_loc = map_item.split(" = ")[0]
        possible_dest = map_item.split(" = ")[1].replace("(", "")
        possible_dest_l = possible_dest.split(", ")[0].replace("(", "")
        possible_dest_r = possible_dest.split(", ")[1].replace(")", "")
        map[cur_loc] = [possible_dest_l, possible_dest_r]
    start = "AAA"

    for i, step in enumerate(steps):
        if i == 0:
            new_direction = "AAA"
        if step == "L":
            new_direction = map[new_direction][1]
        else:
            new_direction = map[new_direction][0]


assert new_direction == "BBB"
