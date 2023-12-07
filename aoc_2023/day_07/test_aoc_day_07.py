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

def test_strength():
    hand = "AAAAA"
    hand = [mapping[c] for c in hand]
    hand = set(hand)
    rel_strength = 0
    for i in hand:
        rel_strength += i*i
    assert rel_strength == 169



def test_get_total_winnings():
    total_winnings = 0
    assert total_winnings == 6440