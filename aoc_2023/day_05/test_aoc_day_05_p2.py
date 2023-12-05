from test_aoc_day_05 import create_map, get_mapping
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
    lines = data.split("\n\n")
    seeds = lines[0].split(": ")[1].split(" ")
    seeds = [int(s) for s in seeds]
    new_seeds = []
    for i, seed in enumerate(seeds[::2]):
        seed_range = seeds[2*i+1]
        for j in range(seed, seed + seed_range):
            new_seeds.append(j)
    assert new_seeds == [79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67]


def test_seed_to_location():
    with open("aoc_data_05.txt", "r") as f:
        real_data = f.read()
    #real_data = data
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
    new_seeds = []
    for i, seed in enumerate(seeds[::2]):
        seed_range = seeds[2 * i + 1]
        for j in range(seed, seed + seed_range):
            new_seeds.append(j)

    for seed in new_seeds:
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

    assert lowest_location == 46