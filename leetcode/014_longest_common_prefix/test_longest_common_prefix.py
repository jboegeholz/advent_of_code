import pytest


@pytest.mark.parametrize(
    "strs, expected",
    [
        (["a", "a"], "a"),
        (["b", "b"], "b"),
        (["c", "c"], "c"),
        (["aa", "aa"], "aa"),
        (["aaa", "aaa"], "aaa"),
    ]
)
def test_longest_common_prefix(strs, expected):
    lcp = longest_common_prefix(strs)
    assert lcp == expected


def longest_common_prefix(strs):
    num_of_strings = len(strs)


def test_sort_strings():
    strs = ["abcd", "abc", "ab", "a"]
    strs.sort()
    assert strs == ["a", "ab", "abc", "abcd"]
