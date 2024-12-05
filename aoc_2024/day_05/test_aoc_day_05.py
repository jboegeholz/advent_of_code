import pytest
data = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

def test_split_data():
    rules = data.split("\n\n")[0].split("\n")
    pages = data.split("\n\n")[1]
    assert rules

def test_convert_rules_to_dict():
    rule = "97|75"
    rules_dict = {int(rule.split("|")[1]): int(rule.split("|")[0])}
    assert {75: 97} == rules_dict

@pytest.mark.parametrize(
    "input, expected",
    [
        ("75,47,61,53,29", True),
        ("75,97,47,61,53", False),

    ]
)
def test_is_correct_order(input, expected):
    rules = {75: 97}
    correct_order = True
    pages = [int(x) for x in input.split(",")]
    for i, page in enumerate(pages):
        for j in range(len(pages)):
            if page in rules and rules[page] == pages[j]:
                correct_order = False
                break

    assert correct_order == expected



