import pytest


@pytest.mark.parametrize(
    "roman, expected",
    [
        ("I", 1),
        ("II", 2),
        ("III", 3),
        ("IV", 4),
        ("X", 10),
        ("L", 50),
        ("C", 100),
        ("D", 500),
        ("M", 1000),
    ]
)
def test_roman_literals(roman, expected):
    assert expected == roman_literals(roman)


def roman_literals(roman):
    num = 0
    if "IV" in roman:
        roman = roman.replace("IV", "IIII")
    for c in roman:
        if c == "I":
            num += 1
        if c == "X":
            num += 10
        if c == "L":
            num += 50
        if c == "C":
            num += 100
        if c == "D":
            num += 500
        if c == "M":
            num += 1000
    return num
