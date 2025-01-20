import pytest

@pytest.mark.parametrize(
    "input, expected",
    [
        (121, True),
        (-121, False),
        (10, False),
    ]
)
def test_is_palindrome(input, expected):
    palindrome = is_palindrome(input)
    assert palindrome == expected


def is_palindrome(x):
    l1 = list(str(x))
    palindrome = True
    j = len(l1) - 1
    for i in range(len(l1)):
        if l1[i] != l1[j]:
            palindrome = False
        if i == j:
            break
        else:
            j -= 1
    return palindrome