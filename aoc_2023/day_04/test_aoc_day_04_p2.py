data = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""


def test_get_total_points():
    lines = data.split("\n")
    cardsnwins = [
        # card, no of cards, wins,
        [0, 0, 0]]
    for card_no, line in enumerate(lines):
        wins = 0
        numbers = line.split(": ")[1]
        winning_numbers = numbers.split(" | ")[0].replace("  ", " ").split(" ")
        your_numbers = numbers.split(" | ")[1].replace("  ", " ").split(" ")
        for your_number in your_numbers:
            if your_number in winning_numbers:
                wins += 1
        cardsnwins.append([card_no+1, 1, wins])
    # postprocessing
    for j in range(0, len(cardsnwins)-3):
        for i in range(2+j, cardsnwins[1+j][2]+2+j):
            cardsnwins[i][1] += cardsnwins[1+j][1]
    sum_of_cards = 0
    for card in cardsnwins:
        sum_of_cards += card[1]
    assert sum_of_cards == 30


def test_wins():
    cardsnwins = [
        # card, no of cards, wins,
        [0, 0, 0],
        [1, 1, 4],
        [2, 1, 2],
        [3, 1, 2],
        [4, 1, 1],
        [5, 1, 0],
        [6, 1, 0]
    ]

    for j in range(0, len(cardsnwins)-3):
        for i in range(2+j, cardsnwins[1+j][2]+2+j):
            cardsnwins[i][1] += cardsnwins[1+j][1]


    assert cardsnwins == [
        # card, no of cards, wins,
        [0, 0, 0],
        [1, 1, 4],
        [2, 2, 2],
        [3, 4, 2],
        [4, 8, 1],
        [5, 14, 0],
        [6, 1, 0]
    ]
    sum_of_cards = 0
    for card in cardsnwins:
        sum_of_cards += card[1]
    assert sum_of_cards == 30