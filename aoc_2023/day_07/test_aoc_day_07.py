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
    "A": 13,
           }
def test_convert_hand():
    hand = "AAAAA"
    hand = [mapping[c] for c in hand]
    assert hand == [13, 13, 13, 13, 13]

@pytest.mark.parametrize(
    "hand, exp_hand_class",
    [
        # five oak
        ("AAAAA", 7),
        ("22222", 7),
        # four oak
        ("AAAAQ", 6),
        ("2222A", 6),
        # full house
        ("AAAQQ", 5),
        ("22233", 5),
        # three oak
        ("AAAQJ", 4),
        ("22234", 4),
        # two pair
        ("AAQQJ", 3),
        ("22334", 3),
        # one pair
        ("AAQJT", 2),
        ("22345", 2),
        # # high card
        # ("AJQT9", 1),
        # ("65432", 1),


    ]
)
def test_get_class(hand, exp_hand_class):
    hand_class = 0
    hand = [mapping[c] for c in hand]
    hand.sort(reverse=True)
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

    assert hand_class == exp_hand_class



def test_get_total_winnings():
    total_winnings = 0
    assert total_winnings == 6440