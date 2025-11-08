import pytest


class TestBestTimeToBuyStocks:
    """
    You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
    On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can sell and buy the stock multiple times on the same day, ensuring you never hold more than one share of the stock.
    Find and return the maximum profit you can achieve.
    Example 1:
    Input: prices = [7,1,5,3,6,4]
    Output: 7
    Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
    Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
    Total profit is 4 + 3 = 7.
    Example 2:
    Input: prices = [1,2,3,4,5]
    Output: 4
    Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
    Total profit is 4.
    Example 3:
    Input: prices = [7,6,4,3,1]
    Output: 0
    Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
    Constraints:
    1 <= prices.length <= 3 * 104
    0 <= prices[i] <= 104
    """

    def best_time(self, prices: list[int]) -> int:
        # # greedy O(n) time and O(1) space:
        #  profit = 0
        #
        #  for i in range(1, len(prices)):
        #      if prices[i] > prices[i - 1]:
        #          profit += prices[i] - prices[i - 1]
        #
        #  return profit

        # # dp table O(n) time and O(n) space:
        # n = len(prices)
        # dp = [[0, 0] for _ in range(n)]
        # dp[0][0] = 0
        # dp[0][1] = -prices[0]
        # for i in range(1, n):
        #     dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
        #     dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        # return dp[-1][0]

        # dp 2 vars O(n) time and O(1) space:
        hold = -prices[0]
        cash = 0
        for price in prices[1:]:
            cash = max(cash, hold + price)  # sell
            hold = max(hold, cash - price)  # buy

        return cash

    @pytest.mark.parametrize("prices, expected", [
        ([7, 1, 5, 3, 6, 4], 7),
        ([1, 2, 3, 4, 5], 4),
        ([7, 6, 4, 3, 1], 0),

    ])
    def test_best_time(self, prices, expected):
        assert self.best_time(prices) == expected
