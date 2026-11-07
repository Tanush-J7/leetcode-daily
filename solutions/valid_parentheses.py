class Solution:
    def isValid(self, s: str) -> bool:
        """Return whether the brackets in s are properly matched.

        Runs in O(n) time and uses O(n) extra space.
        """
        matching = {')': '(', ']': '[', '}': '{'}
        stack = []

        for char in s:
            if char in matching:
                if not stack or stack.pop() != matching[char]:
                    return False
            else:
                stack.append(char)

        return not stack
