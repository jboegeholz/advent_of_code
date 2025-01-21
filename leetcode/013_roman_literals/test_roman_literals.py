import pytest

@pytest.mark.parametrize(
    "roman, expected",
    [
        ("I", 1),
        ("II", 2),
        ("III", 3),
        ("IV", 4),
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
    return num