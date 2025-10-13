import pytest
class TestByuSellStocks:
    """Medium
    Topics
    premium lock icon
    Companies
    Hint
    You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.
    Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.
    Note:
    You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
    The transaction fee is only charged once for each stock purchase and sale.

    Example 1:
    Input: prices = [1,3,2,8,4,9], fee = 2
    Output: 8
    Explanation: The maximum profit can be achieved by:
    - Buying at prices[0] = 1
    - Selling at prices[3] = 8
    - Buying at prices[4] = 4
    - Selling at prices[5] = 9
    The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
    Example 2:
    Input: prices = [1,3,7,5,10,3], fee = 3
    Output: 6
    Constraints:
    1 <= prices.length <= 5 * 104
    1 <= prices[i] < 5 * 104
    """
    def buy_sell_stocks(self, prices: list[int], fee: int) -> int:
        hold = -prices[0] # bought on day 1
        cash = 0 # no profit just started

        for price in prices[1:]:
            hold = max(hold, cash - price)
            cash = max(cash, hold + price - fee)

        return cash

    @pytest.mark.parametrize("prices, fee, expected", [
        ([1, 3, 2, 8, 4, 9], 2, 8),
        ([1, 3, 7, 5, 10, 3], 3, 6),
    ])
    def test_buy_sell_stocks(self, prices, fee, expected):
        assert self.buy_sell_stocks(prices, fee) == expected