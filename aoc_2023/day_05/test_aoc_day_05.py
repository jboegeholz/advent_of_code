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
    # create map
    seed_to_soil_entry = lines[1].split("\n")
    seed_to_soil_data = seed_to_soil_entry[1:]
    seed_to_soil_map = []
    for line in seed_to_soil_data:
        seed_to_soil_map.append([int(s) for s in line.split(" ")])
    # get mapping seed -> soil
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


@pytest.mark.parametrize(
    "seed, exp_soil, exp_fert, exp_wat, exp_light, exp_temp, exp_hum, exp_loc",
    [
        (79, 81, 81, 81, 74, 78, 78, 82),
        (14, 14, 53, 49, 42, 42, 43, 43),
        (55, 57, 57, 53, 46, 82, 82, 86)

    ]
)
def test_seed_to_location(seed, exp_soil, exp_fert, exp_wat, exp_light, exp_temp, exp_hum, exp_loc):
    lines = data.split("\n\n")
    # create maps
    seed_to_soil_map = create_map(lines, 1)
    soil_to_fertilizer_map = create_map(lines, 2)
    fertilizer_to_water_map = create_map(lines, 3)
    water_to_light_map = create_map(lines, 4)
    light_to_temperature_map = create_map(lines, 5)
    temperature_to_humidity_map = create_map(lines, 6)
    humidity_to_location_map = create_map(lines, 7)

    # get mapp9ing
    soil = get_mapping(seed, seed_to_soil_map)
    fertilizer = get_mapping(soil, soil_to_fertilizer_map)
    water = get_mapping(fertilizer, fertilizer_to_water_map)
    light = get_mapping(water, water_to_light_map)
    temperature = get_mapping(light, light_to_temperature_map)
    humidity = get_mapping(temperature, temperature_to_humidity_map)
    location = get_mapping(humidity, humidity_to_location_map)
    assert soil == exp_soil
    assert fertilizer == exp_fert
    assert water == exp_wat
    assert light == exp_light
    assert temperature == exp_temp
    assert humidity == exp_hum
    assert location == exp_loc


def test_seed_to_location():
    with open("aoc_data_05.txt", "r") as f:
        real_data = f.read()
    # get seeds
    lines = real_data.split("\n\n")
    seeds = lines[0].split(": ")[1].split(" ")
    seeds = [int(s) for s in seeds]
    # create maps
    seed_to_soil_map = create_map(lines, 1)
    soil_to_fertilizer_map = create_map(lines, 2)
    fertilizer_to_water_map = create_map(lines, 3)
    water_to_light_map = create_map(lines, 4)
    light_to_temperature_map = create_map(lines, 5)
    temperature_to_humidity_map = create_map(lines, 6)
    humidity_to_location_map = create_map(lines, 7)

    lowest_location = 2**32
    for seed in seeds:
    # get mapping
        soil = get_mapping(seed, seed_to_soil_map)
        fertilizer = get_mapping(soil, soil_to_fertilizer_map)
        water = get_mapping(fertilizer, fertilizer_to_water_map)
        light = get_mapping(water, water_to_light_map)
        temperature = get_mapping(light, light_to_temperature_map)
        humidity = get_mapping(temperature, temperature_to_humidity_map)
        location = get_mapping(humidity, humidity_to_location_map)
        if location < lowest_location:
            lowest_location = location

    assert lowest_location == 12

def get_mapping(source, map):
    for sts in map:
        destination_start = sts[0]
        source_start = sts[1]
        range = sts[2]
        if source_start <= source <= source_start + range:
            offset = source - sts[1]
            dest = destination_start + offset
            break
        else:
            dest = source
    return dest


def create_map(lines, index):
    _map = []
    _entry = lines[index].split("\n")
    _data = _entry[1:]
    for line in _data:
        _map.append([int(s) for s in line.split(" ")])
    return _map


def test_get_total_points_from_real_data():
    with open("aoc_data_05.txt", "r") as f:
        real_data = f.read()

    assert True


