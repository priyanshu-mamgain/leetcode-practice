class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = {}

        # Count each character
        for char in s:
            count[char] = count.get(char, 0) + 1

        length = 0
        has_odd = False

        # Use pairs
        for value in count.values():
            length += (value // 2) * 2

            if value % 2 == 1:
                has_odd = True

        # One odd character can go in the middle
        if has_odd:
            length += 1

        return length