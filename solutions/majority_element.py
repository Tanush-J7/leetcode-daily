from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """Return the majority element (appears more than n/2 times).

        Boyer-Moore Voting Algorithm
        Runs in O(n) time and uses O(1) extra space.
        """
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            elif candidate == num:
                count += 1
            else:
                count -= 1

        return candidate
