def test_with_real_data():
    race = [44707080, 283113411341491]
    prod_ways_to_win = 1
    distances = []
    for i in range(race[0] + 1):
        distance_travelled = (race[0]  - i) * i
        if distance_travelled > race[1] :
            distances.append(distance_travelled)
    ways_to_win = len(distances)
    assert ways_to_win == 29432455