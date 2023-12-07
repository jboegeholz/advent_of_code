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
    "hand, exp_hand_class, exp_strength",
    [
        # five oak
        ("AAAAA", 7, 10000065),
        ("22222", 7, 10000010),
        # four oak
        ("AAAAQ", 6, 1000064),
        ("2222A", 6, 1000021),
        # full house
        ("AAAQQ", 5, 100063),
        ("22233", 5, 100012),
        # three oak
        ("AAAQJ", 4, 10062),
        ("22234", 4, 10013),
        # two pair
        ("AAQQJ", 3, 1061),
        ("22334", 3, 1014),
        # one pair
        ("AAQJT", 2, 159),
        ("22345", 2, 116),
        # # high card
        ("AJQT9", 1, 65),
        ("65432", 1, 30),


    ]
)
def test_get_class(hand, exp_hand_class, exp_strength):
    hand_class = 0
    hand = [mapping[c] for c in hand]
    hand.sort(reverse=True)
    hand_class = get_class(hand, hand_class)
    strength = get_absolute_strength(hand, hand_class, strength)
    assert hand_class == exp_hand_class
    assert exp_strength == strength


def get_absolute_strength(hand, hand_class, strength):
    for i in hand:
        strength += i
    strength += 10 ** hand_class
    return strength


def get_class(hand, hand_class):
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
    assert total_winnings == 6440