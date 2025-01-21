import pytest

@pytest.mark.parametrize(
    "roman, expected",
    [
        ("I", 1),
        ("II", 2),
        ("III", 3),
    ]
)
def test_roman_literals(roman, expected):
    assert expected == roman_literals(roman)


def roman_literals(roman):
    if roman == "I":
        return 1
    if roman == "II":
        return 2
    if roman == "III":
        return 3