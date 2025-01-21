import pytest


@pytest.mark.parametrize(
    "input, expected",
    [
        (1, "I"),
        (40, "XL"),
        (1984, "MCMLXXXIV"),
    ]
)
def test_int_to_roman(input, expected):
    assert expected == convert_number(input)

def convert_number_simple(number):
    roman_literal = ""
    thousands = number // 1000
    roman_literal += "M" * thousands
    five_hundreds = number % 1000 // 500
    roman_literal += "D" * five_hundreds
    hundreds = number % 1000 % 500 // 100
    roman_literal += "C" * hundreds
    fifties = number % 1000 % 500 % 100 // 50
    roman_literal += "L" * fifties
    tens = number % 1000 % 500 % 100 % 50 // 10
    roman_literal += "X" * tens
    fives = number % 1000 % 500 % 100 % 50 % 10 // 5
    roman_literal += "V" * fives
    ones = number % 1000 % 500 % 100 % 50 % 10 % 5
    roman_literal += "I" * ones
    return roman_literal

def convert_number(roman_literal):
    roman_literal = convert_number_simple(roman_literal)
    roman_literal = roman_literal.replace("DCCCC", "CM") # 900
    roman_literal = roman_literal.replace("CCCC", "CD") # 400
    roman_literal = roman_literal.replace("LXXXX", "XC") # 90
    roman_literal = roman_literal.replace("XXXX", "XL") # 40
    roman_literal = roman_literal.replace("VIIII", "IX") # 9
    roman_literal = roman_literal.replace("IIII", "IV")  # 4
    return roman_literal