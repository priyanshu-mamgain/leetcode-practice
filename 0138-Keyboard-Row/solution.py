
from traitlets import List

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")

        result = []

        for word in words:
            lower_word = word.lower()

            if all(char in row1 for char in lower_word):
                result.append(word)
            elif all(char in row2 for char in lower_word):
                result.append(word)
            elif all(char in row3 for char in lower_word):
                result.append(word)

        return result
