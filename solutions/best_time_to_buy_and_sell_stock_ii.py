from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """Return maximum profit by buying/selling multiple times.

        Strategy: whenever the next day is higher than today, buy and sell.
        Runs in O(n) time and uses O(1) extra space.
        """
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit
