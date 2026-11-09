from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """Return True if any value appears at least twice.

        Runs in O(n) time and uses O(n) extra space.
        """
        return len(nums) != len(set(nums))
