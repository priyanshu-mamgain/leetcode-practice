class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""

        result = ""

        while sum >= 9:
            result += "9"
            sum -= 9

        if sum > 0:
            result += str(sum)

        result += "0" * (num - len(result))

        return result