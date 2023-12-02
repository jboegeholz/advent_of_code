data = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""


def test_check_power_of_game():
    power_of_game = 1
    line = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    games = line.split(": ")[1].split("; ")
    maximum_red = 0
    maximum_green = 0
    maximum_blue = 0
    for game in games:
        colors = game.split(", ")
        for color in colors:
            if "red" in color:
                num_of_red = color.split(" ")[0]
                if int(num_of_red) > maximum_red:
                    maximum_red = int(num_of_red)
            if "green" in color:
                num_of_green = color.split(" ")[0]
                if int(num_of_green) > maximum_green:
                    maximum_green = int(num_of_green)
            if "blue" in color:
                num_of_blue = color.split(" ")[0]
                if int(num_of_blue) > maximum_blue:
                    maximum_blue = int(num_of_blue)
    power_of_game = maximum_red * maximum_green * maximum_blue
    assert power_of_game == 48


def test_check_power_of_game():
    with open("aoc_data_02.txt", "r") as f:
        data = f.read()
    sum_of_power_of_gams = 0
    for line in data.split("\n"):
        games = line.split(": ")[1].split("; ")
        maximum_red = 0
        maximum_green = 0
        maximum_blue = 0
        for game in games:
            colors = game.split(", ")
            for color in colors:
                if "red" in color:
                    num_of_red = color.split(" ")[0]
                    if int(num_of_red) > maximum_red:
                        maximum_red = int(num_of_red)
                if "green" in color:
                    num_of_green = color.split(" ")[0]
                    if int(num_of_green) > maximum_green:
                        maximum_green = int(num_of_green)
                if "blue" in color:
                    num_of_blue = color.split(" ")[0]
                    if int(num_of_blue) > maximum_blue:
                        maximum_blue = int(num_of_blue)
        power_of_game = maximum_red * maximum_green * maximum_blue
        sum_of_power_of_gams += power_of_game
    assert sum_of_power_of_gams == 54911
