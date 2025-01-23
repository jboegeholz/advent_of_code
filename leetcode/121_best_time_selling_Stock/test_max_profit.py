import pytest


@pytest.mark.parametrize(
    "prices, exp_profit",
    [
        ([1, 2], 1),
        ([1, 2, 3], 2),
        ([7,1,5,3,6,4], 5),
        ([7,6,4,3,1], 0),

    ]
)
def test_max_profit(prices, exp_profit):
    max_profit = calc_max_profit(prices)
    assert max_profit == exp_profit


def calc_max_profit(prices):
    left, right = 0, 1
    max_profit = 0
    while right < len(prices):
        if prices[left] < prices[right]:
            profit = prices[right] - prices[left]
            max_profit = max(profit, max_profit)
        else:
            left = right
        right += 1
    return max_profit