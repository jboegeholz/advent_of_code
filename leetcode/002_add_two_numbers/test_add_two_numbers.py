"""
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
"""
def test_add_two_numbers():
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    num1 = 0
    num2 = 0
    for i in reversed(range(0, len(l1))):
        num1 += l1[i] * 10 ** i
        num2 += l2[i] * 10 ** i
    assert num1 == 342
    assert num2 == 465

def test_add_two_numbers2():
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    num1 = 0
    num2 = 0
    for i in reversed(range(0, len(l1))):
        num1 += l1[i] * 10 ** i
        num2 += l2[i] * 10 ** i
    assert num1 == 342
    assert num2 == 465