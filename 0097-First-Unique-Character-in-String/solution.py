class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}

        # Count how many times each character appears
        for char in s:
            count[char] = count.get(char, 0) + 1

        # Find the first character that appears only once
        for i in range(len(s)):
            if count[s[i]] == 1:
                return i

        return -1