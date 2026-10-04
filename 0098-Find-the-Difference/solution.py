class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count = [0] * 26

        for char in s:
            count[ord(char) - ord('a')] += 1

        for char in t:
            index = ord(char) - ord('a')

            if count[index] == 0:
                return char

            count[index] -= 1

        return ""