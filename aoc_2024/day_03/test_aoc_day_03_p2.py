import re
def test_regex():
    text = "Dies ist ein start Text mit Inhalten end, die entfernt werden sollen."
    result = re.sub(r'(?<=start).*?(?=end)', '', text)
    assert result == "Dies ist ein startend, die entfernt werden sollen."

def test_remove_sections():
    # The do() instruction enables future mul instructions.
    # The don't() instruction disables future mul instructions.
    data = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    data = re.sub(r"don't\(\).+do\(\)", '', data)

    assert data == "xmul(2,4)&mul[3,7]!^?mul(8,5))"

def test_regex_full_data_multiply():
    with open("aoc_data_03.txt", "r") as f:
        data = f.read()
        p = re.compile(r"mul\(\d+,\d+\)")
        result = p.findall(data)
        sum_of_products = 0
        p = re.compile(r"mul\(\d+,\d+\)")
        result = p.findall(data)
        for instruction in result:
            splitted = instruction.split("mul(")
            numbers = splitted[1].rstrip(")").split(",")
            product = int(numbers[0]) * int(numbers[1])
            sum_of_products += product

        assert sum_of_products == 0