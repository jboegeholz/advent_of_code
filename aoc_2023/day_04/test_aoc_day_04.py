data = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""


def test_get_cards():
    line = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
    numbers = line.split(": ")[1]
    assert numbers == "41 48 83 86 17 | 83 86  6 31 17  9 48 53"

def test_get_winning_numbers():
    line = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
    numbers = line.split(": ")[1]
    winning_numbers = numbers.split(" | ")[0]
    your_numbers = numbers.split(" | ")[1]
    assert winning_numbers == "41 48 83 86 17"
    assert your_numbers == "83 86  6 31 17  9 48 53"


def test_numbers_to_list():
    line = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
    numbers = line.split(": ")[1]
    winning_numbers = numbers.split(" | ")[0].replace("  ", " ").split(" ")
    your_numbers = numbers.split(" | ")[1].replace("  ", " ").split(" ")

    assert winning_numbers == ['41', '48', '83', '86', '17']
    assert your_numbers == ['83', '86', '6', '31', '17', '9', '48', '53']

def test_get_wins():
    line = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
    wins = 0
    numbers = line.split(": ")[1]
    winning_numbers = numbers.split(" | ")[0].replace("  ", " ").split(" ")
    your_numbers = numbers.split(" | ")[1].replace("  ", " ").split(" ")
    for your_number in your_numbers:
        if your_number in winning_numbers:
            wins +=1
    assert wins == 4
    assert 2**(wins-1) == 8

def test_get_total_points():
    lines = data.split("\n")
    total_points = 0
    for line in lines:
        wins = 0
        numbers = line.split(": ")[1]
        winning_numbers = numbers.split(" | ")[0].replace("  ", " ").split(" ")
        your_numbers = numbers.split(" | ")[1].replace("  ", " ").split(" ")
        for your_number in your_numbers:
            if your_number in winning_numbers:
                wins +=1
        if wins > 0:
            points = 2**(wins-1)
            total_points += points
    assert total_points == 13


