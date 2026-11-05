from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """Return the best profit from one buy and one later sell.

        Runs in O(n) time and uses O(1) extra space.
        """
        lowest_price = float("inf")
        best_profit = 0

        for price in prices:
            lowest_price = min(lowest_price, price)
            best_profit = max(best_profit, price - lowest_price)

        return best_profit
