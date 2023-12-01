import pytest

data = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""


def test_fully_contain_assignment_split():
    assignments = data.split("\n")
    assert assignments == ['2-4,6-8', '2-3,4-5', '5-7,7-9', '2-8,3-7', '6-6,4-6', '2-6,4-8']
    first_assignment = assignments[0].split(",")
    assert first_assignment == ['2-4', '6-8']

def test_fully_contain_assignment():
    contains = 0
    assignments = data.split("\n")
    for assignment in assignments:
        first_assignment_pair = assignment.split(",")
        fa = first_assignment_pair[0].split("-")
        sa = first_assignment_pair[1].split("-")
        if fa[0] >= sa[0] and fa[1] <= sa[1]:
            contains += 1
        elif fa[0] <= sa[0] and fa[1] >= sa[1]:
            contains += 1
    assert contains == 2

@pytest.mark.parametrize(
    "data, expected",
    [
        ("2-4,6-8", 0),
        ("2-3,4-5", 0),
        ("5-7,7-9", 0),
        ("2-8,3-7", 1),
        ("6-6,4-6", 2),
        ("2-6,4-8", 0),
        ("7-96,6-95", 0),
    ]
)
def test_fully_split(data, expected):
    contains = 0
    first_assignment_pair = data.split(",")
    fa = first_assignment_pair[0].split("-")
    fa = [int(x) for x in fa]
    sa = first_assignment_pair[1].split("-")
    sa = [int(x) for x in sa]
    # first contains second
    if fa[0] <= sa[0] and fa[1] >= sa[1]:
        contains += 1
    elif sa[0] <= fa[0] and sa[1] >= fa[1]:
        contains += 2
    assert contains == expected


def test_fully_contain_assignment_from_file():
    with open("aoc_data_04.txt", "r") as f:
        data = f.read()
    contains = 0
    assignments = data.split("\n")
    for assignment in assignments:
        first_assignment_pair = assignment.split(",")
        fa = first_assignment_pair[0].split("-")
        fa = [int(x) for x in fa]
        sa = first_assignment_pair[1].split("-")
        sa = [int(x) for x in sa]
        if fa[0] <= sa[0] and fa[1] >= sa[1]:
            contains += 1
        elif sa[0] <= fa[0] and sa[1] >= fa[1]:
            contains += 1
    assert contains == 490
