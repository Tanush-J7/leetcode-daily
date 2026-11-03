from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """Return indices of two numbers whose sum is target.

        Runs in O(n) time and uses O(n) extra space.
        """
        seen = {}
        for index, value in enumerate(nums):
            complement = target - value
            if complement in seen:
                return [seen[complement], index]
            seen[value] = index
        return []
