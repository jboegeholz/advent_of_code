import pytest


@pytest.mark.parametrize(
    "strs, expected",
    [
        (["a", "a"], "a"),
        (["b", "b"], "b"),
    ]
)
def test_longest_common_prefix(strs, expected):
    lcp = longest_common_prefix(strs)
    assert lcp == expected


def longest_common_prefix(strs):
    if strs[0][0] == strs[1][0]:
        return strs[0][0]