class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)

        vowels = "aeiouAEIOU"

        left = 0
        right = len(s) - 1

        while left < right:
            # Move left until we find a vowel
            while left < right and s[left] not in vowels:
                left += 1

            # Move right until we find a vowel
            while left < right and s[right] not in vowels:
                right -= 1

            # Swap the vowels
            s[left], s[right] = s[right], s[left]

            left += 1
            right -= 1

        return "".join(s)