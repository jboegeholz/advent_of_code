import re

def test_mul_simple():
    data = "mul(44,46)"
    splitted = data.split("mul(")
    numbers = splitted[1].rstrip(")").split(",")
    product = int(numbers[0]) * int(numbers[1])
    assert product == 2024



