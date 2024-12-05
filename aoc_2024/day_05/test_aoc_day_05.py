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
    rules = """97|13
61|13
75|13""".split("\n")
    rules_dict = rules_to_dict(rules)
    assert {13: [97, 61, 75]} == rules_dict


def test_convert_all_rules_to_dict():
    rules = data.split("\n\n")[0].split("\n")
    rules_dict = rules_to_dict(rules)
    assert {13: [97, 61, 29, 47, 75, 53],
 29: [75, 97, 53, 61, 47],
 47: [97, 75],
 53: [47, 75, 61, 97],
 61: [97, 47, 75],
 75: [97]} == rules_dict


def rules_to_dict(rules):
    rules_dict = {}
    for rule in rules:
        key = int(rule.split("|")[1])
        value = int(rule.split("|")[0])
        if not key in rules_dict:
            rules_dict[key] = []
        rules_dict[key].append(value)
    return rules_dict


@pytest.mark.parametrize(
    "input, expected",
    [
        ("75,47,61,53,29", True),
        ("75,97,47,61,53", False),

    ]
)
def test_is_correct_order(input, expected):
    rules = data.split("\n\n")[0].split("\n")
    rules_dict = rules_to_dict(rules)
    correct_order = True
    pages = [int(x) for x in input.split(",")]
    for i, page in enumerate(pages):
        for j in range(len(pages)):
            if page in rules_dict:
                for rule in rules_dict[page]:
                    if rule == pages[j]:
                        correct_order = False
                        break
            break

    assert correct_order == expected
