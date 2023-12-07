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


def test_shit():
    hands = []
    lines = data.split("\n")
    for line in lines:
        hand = [mapping[c] for c in line.split(" ")[0]]
        hand.sort(reverse=True)
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
    print("comparing ", a, " and ", b)
    hand_class_a = get_class(a[0])
    hand_class_b = get_class(b[0])
    if hand_class_a > hand_class_b:
        return 1
    elif hand_class_a < hand_class_b:
        return -1
    else:
        for i in range(5):
            if a[0][i] > b[0][i]:
                return 1
            elif a[0][i] < b[0][i]:
                return -1
        return 0

def get_class(hand):
    if hand[0] == hand[1] == hand[2] == hand[3] == hand[4]:
        hand_class = 7
    elif hand[0] == hand[1] == hand[2] == hand[3]:
        hand_class = 6
    elif hand[1] == hand[2] == hand[3] == hand[4]:
        hand_class = 6
    elif (hand[0] == hand[1]) and (hand[2] == hand[3] == hand[4]):
        hand_class = 5
    elif (hand[0] == hand[1] == hand[2]) and (hand[3] == hand[4]):
        hand_class = 5
    elif hand[0] == hand[1] == hand[2]:
        hand_class = 4
    elif hand[1] == hand[2] == hand[3]:
        hand_class = 4
    elif hand[2] == hand[3] == hand[4]:
        hand_class = 4
    elif hand[0] == hand[1] and hand[2] == hand[3]:
        hand_class = 3
    elif hand[0] == hand[1] and hand[3] == hand[4]:
        hand_class = 3
    elif hand[1] == hand[2] and hand[3] == hand[4]:
        hand_class = 3
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
    return hand_class