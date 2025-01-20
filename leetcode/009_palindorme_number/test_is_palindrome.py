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
    # pragmatic approach
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

def test_reverse_number():
    num = 123
    reverse = reverse_number(num)
    assert reverse == 321


def reverse_number(num):
    reverse = 0
    while num > 0:
        last_digit = num % 10
        reverse = reverse * 10 + last_digit
        num = num // 10
    return reverse


def test_is_palindrome_with_reverse():
    old = 121

    assert isPalindrome(old)

def isPalindrome(x: int) -> bool:
    # sped up version
    reverse = 0
    num = x
    while num > 0:
        last_digit = num % 10
        reverse = reverse * 10 + last_digit
        num = num // 10
    if (x - reverse) == 0:
        palindrome = True
    else:
        palindrome = False
    return palindrome