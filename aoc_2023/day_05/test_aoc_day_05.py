import pytest

data = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""


def test_get_seeds():
    lines = data.split("\n")
    seeds = lines[0].split(": ")[1].split(" ")
    seeds = [int(s) for s in seeds]
    assert seeds == [79, 14, 55, 13]

def test_get_destination_start_range():
    lines = data.split("\n\n")
    seed_to_soil_entry = lines[1].split("\n")
    seed_to_soil_data = seed_to_soil_entry[1:]
    seed_to_soil_map = []
    for line in seed_to_soil_data:
        seed_to_soil_map.append([int(s) for s in line.split(" ")])

    assert seed_to_soil_map == [[50, 98, 2], [52, 50, 48]]

@pytest.mark.parametrize(
    "seed, expected_soil",
    [
        (98, 50),
        (79, 81),
        (55, 57),
        (13, 13),

    ]
)
def test_seed_to_soil(seed, expected_soil):
    lines = data.split("\n\n")
    seed_to_soil_entry = lines[1].split("\n")
    seed_to_soil_data = seed_to_soil_entry[1:]
    seed_to_soil_map = []
    for line in seed_to_soil_data:
        seed_to_soil_map.append([int(s) for s in line.split(" ")])

    for sts in seed_to_soil_map:
        destination_start = sts[0]
        source_start = sts[1]
        range = sts[2]
        if source_start <= seed <= source_start + range:
            offset = seed - sts[1]
            soil = destination_start + offset
            break
        else:
            soil = seed
    assert soil == expected_soil

def test_get_total_points_from_real_data():
    with open("aoc_data_05.txt", "r") as f:
        real_data = f.read()

    assert True


