import ray
ray.init()

@ray.remote
def f(x):
    return x * x

futures = [f.remote(i) for i in range(4)]
print(ray.get(futures)) # [0, 1, 4, 9]

def test_seed_to_location():
    with open("aoc_data_05.txt", "r") as f:
        real_data = f.read()
    #real_data = data
    # get seeds
    print("get seeds")
    lines = real_data.split("\n\n")
    seeds = lines[0].split(": ")[1].split(" ")
    seeds = [int(s) for s in seeds]
    print(seeds)
    # create maps
    seed_to_soil_map = create_map(lines, 1)
    soil_to_fertilizer_map = create_map(lines, 2)
    fertilizer_to_water_map = create_map(lines, 3)
    water_to_light_map = create_map(lines, 4)
    light_to_temperature_map = create_map(lines, 5)
    temperature_to_humidity_map = create_map(lines, 6)
    humidity_to_location_map = create_map(lines, 7)

    lowest_location = 2**32


    print(f"Goinf from {seed} to {seed + seed_range}")
    for j in range(seed, seed + seed_range):
        soil = get_mapping(j, seed_to_soil_map)
        fertilizer = get_mapping(soil, soil_to_fertilizer_map)
        water = get_mapping(fertilizer, fertilizer_to_water_map)
        light = get_mapping(water, water_to_light_map)
        temperature = get_mapping(light, light_to_temperature_map)
        humidity = get_mapping(temperature, temperature_to_humidity_map)
        location = get_mapping(humidity, humidity_to_location_map)
        if location < lowest_location:
            lowest_location = location
            print(f"{lowest_location} is lowest location so far")

    assert lowest_location == 46

if __name__ == '__main__':
    test_seed_to_location()
