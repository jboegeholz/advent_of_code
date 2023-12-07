from collections import OrderedDict

import pytest
data="""32T3K 765
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
def test_convert_hand():
    hand = "AAAAA"
    hand = [mapping[c] for c in hand]
    assert hand == [14, 14, 14, 14, 14]

@pytest.mark.parametrize(
    "hand, exp_hand_class, exp_strength",
    [
        # five oak
        ("AAAAA", 7, 10000070),
        ("22222", 7, 10000010),
        # four oak
        ("AAAAQ", 6, 1000068),
        ("2222A", 6, 1000022),
        # full house
        ("AAAQQ", 5, 100066),
        ("22233", 5, 100012),
        # three oak
        ("AAAQJ", 4, 10065),
        ("22234", 4, 10013),
        # two pair
        ("AAQQJ", 3, 1063),
        ("22334", 3, 1014),
        # one pair
        ("AAQJT", 2, 161),
        ("22345", 2, 116),
        # # high card
        ("AJQT9", 1, 66),
        ("65432", 1, 30),


    ]
)
def test_get_class(hand, exp_hand_class, exp_strength):
    hand = [mapping[c] for c in hand]
    hand_class = get_class(sorted(hand, reverse=True))
    strength = get_absolute_strength(hand, hand_class)
    assert hand_class == exp_hand_class
    assert strength == exp_strength


def get_absolute_strength(hand, hand_class):
    strength = 0
    for i in hand:
        strength += i
    strength += 10 ** hand_class
    return strength


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


def test_get_total_winnings():
    total_winnings = 0
    winnings = []
    for line in data.split("\n"):
        orig_hand = line.split(" ")[0]
        bid = line.split(" ")[1]
        hand = [mapping[c] for c in orig_hand]
        hand.sort(reverse=True)
        hand_class = get_class(hand)
        strength = get_absolute_strength(hand, hand_class)
        winnings.append((strength, int(bid), orig_hand))
    winnings.sort(key = lambda x: x[0])
    for rank, w in enumerate(winnings):
        total_winnings += (rank+1) * w[1]

    assert total_winnings == 6440

def test_corner_cases():
    orig_hand_1 = "KTJJT" # KJJTT
    orig_hand_2 = "KK677" # KK776

    strength_1 = get_strength(orig_hand_1)
    strength_2 = get_strength(orig_hand_2)
    assert strength_1 > strength_2


def get_strength(orig_hand):
    hand = [mapping[c] for c in orig_hand]
    hand.sort(reverse=True)
    hand_class = get_class(hand)
    strength = get_absolute_strength(hand, hand_class)
    return strength