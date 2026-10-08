class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)

        for length in range(1, n):
            if n % length != 0:
                continue

            substring = s[:length]
            repetitions = n // length

            if substring * repetitions == s:
                return True

        return False