import pytest
data="""Time:      7  15   30
Distance:  9  40  200"""

@pytest.mark.parametrize(
    "button_pressed_for, expected_distance_travelled",
    [
        (1, 6),
        (2, 10),
        (3, 12),
        (4, 12),
        (5, 10),
        (6, 6),
        (7, 0),


    ]
)
def test_seed_to_soil(button_pressed_for, expected_distance_travelled):
    distance_travelled = (7 - button_pressed_for) * button_pressed_for
    assert distance_travelled == expected_distance_travelled