import pytest

data = """11 - 22, 95 - 115, 998 - 1012, 1188511880 - 1188511890, 222220 - 222224, \
1698522 - 1698528, 446443 - 446449, 38593856 - 38593862, 565653 - 565659, \
824824821 - 824824827, 2121212118 - 2121212124
"""


def test_split_data():
    id_ranges = data.split(',')
    assert len(id_ranges) == 11

def test_sanitize_data():
    id_ranges = data.split(',')
    id_range = id_ranges[0]
    id_range = id_range.strip().split(" - ")
    id_start = int(id_range[0])
    id_end = int(id_range[1])
    assert id_start == 11
    assert id_end == 22

def test_crawl_range():
    invalid_numbers = 0
    for i in range(11, 22+1):
        if str(i)[0] == str(i)[1]:
            invalid_numbers += i

    assert invalid_numbers == 33

def test_find_repeating_pattern():
    assert find_repeating_pattern("11") == '1'
    assert find_repeating_pattern("1010") == '10'

def find_repeating_pattern(s):
    n = len(s)
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            pattern = s[:i]
            if pattern * (n // i) == s:
                return pattern
    return None


def test_solve_riddle():
    invalid_numbers = 0
    id_ranges = data.split(',')
    for id_range in id_ranges:
        id_range = id_range.strip().split(" - ")
        id_start = int(id_range[0])
        id_end = int(id_range[1])
        for i in range(id_start, id_end + 1):
            pattern = find_repeating_pattern(str(i))
            if pattern:
                invalid_numbers += i
    assert invalid_numbers == 1227775554