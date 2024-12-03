import re

def test_mul_simple():
    data = "mul(44,46)"
    splitted = data.split("mul(")
    numbers = splitted[1].rstrip(")").split(",")
    product = int(numbers[0]) * int(numbers[1])
    assert product == 2024

def test_regex():
    data = "mul(44,46)"
    p = re.compile(r"mul\(\d+,\d+\)")
    result = p.findall(data)
    assert result == ['mul(44,46)']

def test_regex_test_data():
    data = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    p = re.compile(r"mul\(\d+,\d+\)")
    result = p.findall(data)
    assert result == ['mul(2,4)', 'mul(5,5)', 'mul(11,8)', 'mul(8,5)']

def test_regex_test_data_multiply():
    data = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    sum_of_products = 0
    p = re.compile(r"mul\(\d+,\d+\)")
    result = p.findall(data)
    for instruction in result:
        splitted = instruction.split("mul(")
        numbers = splitted[1].rstrip(")").split(",")
        product = int(numbers[0]) * int(numbers[1])
        sum_of_products += product
    assert sum_of_products == 161

def test_regex_full_data_multiply():
    with open("aoc_data_03.txt", "r") as f:
        data = f.read()
        sum_of_products = 0
        p = re.compile(r"mul\(\d+,\d+\)")
        result = p.findall(data)
        for instruction in result:
            splitted = instruction.split("mul(")
            numbers = splitted[1].rstrip(")").split(",")
            product = int(numbers[0]) * int(numbers[1])
            sum_of_products += product

        assert sum_of_products == 162813399