class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        left = 0
        max_length = 0

        for right in range(len(s)):
            char = s[right]

            if char in seen and seen[char] >= left:
                left = seen[char] + 1

            seen[char] = right

            length = right - left + 1
            max_length = max(max_length, length)

        return max_length