
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return left + 1, right - 1

        longest = ""

        for i in range(len(s)):
            # Odd-length palindrome
            left, right = expand(i, i)

            if right - left + 1 > len(longest):
                longest = s[left:right + 1]

            # Even-length palindrome
            left2, right2 = expand(i, i + 1)

            if right2 - left2 + 1 > len(longest):
                longest = s[left2:right2 + 1]

        return longest