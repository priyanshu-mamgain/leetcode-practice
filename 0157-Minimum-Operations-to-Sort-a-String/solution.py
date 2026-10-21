class Solution:
    def minOperations(self, s: str) -> int:
        if s == ''.join(sorted(s)):
            return 0

        n = len(s)
        smallest = min(s)
        largest = max(s)

        if s[0] == smallest or s[-1] == largest:
            return 1

        if s[0] == largest and s[-1] == smallest:
            if n == 2:
                return -1

            if smallest in s[1:-1] or largest in s[1:-1]:
                return 2

            return 3

        return 2
