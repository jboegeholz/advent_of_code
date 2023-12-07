from collections import OrderedDict
from functools import cmp_to_key
import pytest

data = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

mapping = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14,
}


def test_with_test_data():
    lines = data.split("\n")
    hands = []

    for line in lines:
        hand = [mapping[c] for c in line.split(" ")[0]]
        #hand.sort(reverse=True)
        bid = int(line.split(" ")[1])
        hands.append([hand, bid])
    # sort
    hands.sort(key=cmp_to_key(compare))
    assert hands == [
        [[13, 10, 3, 3, 2], 765],
        [[13, 11, 11, 10, 10], 220],
        [[13, 13, 7, 7, 6], 28],
        [[11, 10, 5, 5, 5], 684],
        [[14, 12, 12, 12, 11], 483]
    ]
    total_winnings = 0
    for rank, hand in enumerate(hands):
        bid = hand[1]
        total_winnings += bid * (rank+1)

    assert total_winnings == 6440
def compare(a, b):
    #print("comparing ", a, " and ", b)
    hand_class_a = get_class(a[0])
    hand_class_b = get_class(b[0])
    if hand_class_a == hand_class_b == 1:
        if sum(a[0]) > sum(b[0]):
            return 1
        elif sum(a[0]) < sum(b[0]):
            return -1
        else:
            return 0
    if hand_class_a > hand_class_b:
        return 1
    elif hand_class_a < hand_class_b:
        return -1
    else:
        #print("same class: compare single cards")
        for i in range(5):
            if a[0][i] > b[0][i]:
                return 1
            elif a[0][i] < b[0][i]:
                return -1
        else:
            print("shit identical hands")
            return 0

def get_class(hand):
    hand.sort(reverse=True)
    # five oak
    if hand[0] == hand[1] == hand[2] == hand[3] == hand[4]:
        hand_class = 7
    # four oak
    elif hand[0] == hand[1] == hand[2] == hand[3]:
        hand_class = 6
    elif hand[1] == hand[2] == hand[3] == hand[4]:
        hand_class = 6
    # full house
    elif (hand[0] == hand[1]) and (hand[2] == hand[3] == hand[4]):
        hand_class = 5
    elif (hand[0] == hand[1] == hand[2]) and (hand[3] == hand[4]):
        hand_class = 5
    # three oak
    elif hand[0] == hand[1] == hand[2]:
        hand_class = 4
    elif hand[1] == hand[2] == hand[3]:
        hand_class = 4
    elif hand[2] == hand[3] == hand[4]:
        hand_class = 4
    # two pairs
    elif hand[0] == hand[1] and hand[2] == hand[3]:
        hand_class = 3
    elif hand[0] == hand[1] and hand[3] == hand[4]:
        hand_class = 3
    elif hand[1] == hand[2] and hand[3] == hand[4]:
        hand_class = 3
    # one pair
    elif hand[0] == hand[1]:
        hand_class = 2
    elif hand[1] == hand[2]:
        hand_class = 2
    elif hand[2] == hand[3]:
        hand_class = 2
    elif hand[3] == hand[4]:
        hand_class = 2
    else:
        hand_class = 1
    assert hand_class != 0
    return hand_class

def test_with_real_data():
    with open("aoc_data_07.txt", "r") as f:
        real_data = f.read()
    lines = real_data.split("\n")
    hands = []

    for line in lines:
        hand = [mapping[c] for c in line.split(" ")[0]]
        #hand.sort(reverse=True)
        bid = int(line.split(" ")[1])
        hands.append([hand, bid])
    # sort
    hands.sort(key=cmp_to_key(compare))

    total_winnings = 0
    for rank, hand in enumerate(hands):
        bid = hand[1]
        total_winnings += bid * (rank+1)

    assert total_winnings == 6440