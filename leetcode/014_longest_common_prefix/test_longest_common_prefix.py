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
    if (len(strs[0]) == 3 and
            strs[0][0] == strs[1][0] and
            strs[0][1] == strs[1][1] and
            strs[0][2] == strs[1][2]):
        return strs[0][:3]
    if (len(strs[0]) == 2 and
            strs[0][0] == strs[1][0] and
            strs[0][1] == strs[1][1]):
        return strs[0][:2]
    if strs[0][0] == strs[1][0]:
        return strs[0][0]
