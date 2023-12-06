import pytest
test_data="""Time:      7  15   30
Distance:  9  40  200"""
real_data = """Time:        44     70     70     80
Distance:   283   1134   1134   1491"""

def test_get_races():
    races = get_races(test_data)
    assert races == [(7, 9), (15, 40), (30, 200)]


def get_races(data):
    time = data.split("\n")[0].split(":")[1].split(" ")
    time = list(filter(None, time))
    time = [int(s) for s in time]
    distance = data.split("\n")[1].split(":")[1].split(" ")
    distance = list(filter(None, distance))
    distance = [int(s) for s in distance]
    races = list(zip(time, distance))
    return races


@pytest.mark.parametrize(
    "button_pressed_for, expected_distance_travelled",
    [
        (1, 6),
        (2, 10),
        (3, 12),
        (4, 12),
        (5, 10),
        (6, 6),
        (7, 0),


    ]
)
def test_seed_to_soil(button_pressed_for, expected_distance_travelled):
    distance_travelled = (7 - button_pressed_for) * button_pressed_for
    assert distance_travelled == expected_distance_travelled

@pytest.mark.parametrize(
    "race_time, current_record, ways_to_win",
    [
        (7, 9, 4),
        (15, 40, 8),
        (30, 200, 9),

    ]
)
def test_ways_to_win(race_time, current_record, ways_to_win):
    distances = []
    for i in range(race_time+1):
        distance_travelled = (race_time - i) * i
        if distance_travelled > current_record:
            distances.append(distance_travelled)
    assert len(distances) == ways_to_win



@pytest.mark.parametrize(
    "race_time, current_record, ways_to_win",
    [
        (44, 283, 29),
        (70, 1134, 19),
        (80, 1491, 21),

    ]
)
def test_ways_to_win_real_data(race_time, current_record, ways_to_win):
    distances = []
    for i in range(race_time+1):
        distance_travelled = (race_time - i) * i
        if distance_travelled > current_record:
            distances.append(distance_travelled)
    assert len(distances) == ways_to_win

def test_with_real_data():
    prod_ways_to_win = 1

    races = get_races(real_data)
    for race in races:
        distances = []
        ways_to_win = 0
        for i in range(race[0] + 1):
            distance_travelled = (race[0]  - i) * i
            if distance_travelled > race[1] :
                distances.append(distance_travelled)
        ways_to_win = len(distances)
        prod_ways_to_win *= ways_to_win
    assert prod_ways_to_win == 288