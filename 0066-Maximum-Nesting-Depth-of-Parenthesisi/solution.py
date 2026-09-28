class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        max_depth = 0

        for char in s:
            if char == '(':
                depth += 1
                max_depth = max(max_depth, depth)

            elif char == ')':
                depth -= 1

        return max_depth