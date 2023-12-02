data = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

maximum_color_red = 12
maximum_color_green = 13
maximum_color_blue = 14
def test_get_game_id():
    line = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    game_id = line.split(":")[0].split(" ")[1]
    assert game_id == "1"


def test_get_games():
    line = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    game_1 = line.split(": ")[1].split("; ")[0]
    game_2 = line.split(": ")[1].split("; ")[1]
    game_3 = line.split(": ")[1].split("; ")[2]
    assert game_1 == "3 blue, 4 red"
    assert game_2 == "1 red, 2 green, 6 blue"
    assert game_3 == "2 green"

def test_get_num_of_color():
    line = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    game_1 = line.split(": ")[1].split("; ")[0]
    colors_1 = game_1.split(", ")
    for color in colors_1:
        if "red" in color:
            num_of_red = color.split(" ")[0]
        if "green" in color:
            num_of_green = color.split(" ")[0]
        if "blue" in color:
            num_of_blue = color.split(" ")[0]
    assert num_of_blue == "3"
    assert num_of_red == "4"
def test_check_possible():
    line = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    red_possible = True
    green_possible = True
    blue_possible = True
    game_1 = line.split(": ")[1].split("; ")[0]
    colors_1 = game_1.split(", ")
    for color in colors_1:
        if "red" in color:
            num_of_red = color.split(" ")[0]
            if int(num_of_red) > maximum_color_red:
                red_possible = False
        if "green" in color:
            num_of_green = color.split(" ")[0]
            if int(num_of_green) > maximum_color_green:
                green_possible = False
        if "blue" in color:
            num_of_blue = color.split(" ")[0]
            if int(num_of_blue) > maximum_color_blue:
                blue_possible = False
    assert red_possible
    assert green_possible
    assert blue_possible

def test_sum_of_game_ids():
    with open("aoc_data_02.txt", "r") as f:
        data = f.read()
    sum_of_possible_games_ids = 0
    for line in data.split("\n"):
        red_possible = True
        green_possible = True
        blue_possible = True
        game_id = line.split(":")[0].split(" ")[1]
        games = line.split(": ")[1].split("; ")
        for game in games:
            colors = game.split(", ")
            for color in colors:
                if "red" in color:
                    num_of_red = color.split(" ")[0]
                    if int(num_of_red) > maximum_color_red:
                        red_possible = False
                if "green" in color:
                    num_of_green = color.split(" ")[0]
                    if int(num_of_green) > maximum_color_green:
                        green_possible = False
                if "blue" in color:
                    num_of_blue = color.split(" ")[0]
                    if int(num_of_blue) > maximum_color_blue:
                        blue_possible = False
        if red_possible and green_possible and blue_possible:
            sum_of_possible_games_ids += int(game_id)
    assert sum_of_possible_games_ids == 2476



