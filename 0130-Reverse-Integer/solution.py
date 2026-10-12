
class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN = -(2**31)
        INT_MAX = 2**31 - 1

        sign = -1 if x < 0 else 1
        x = abs(x)
        result = 0

        while x > 0:
            digit = x % 10
            result = result * 10 + digit
            x //= 10

        result *= sign

        if result < INT_MIN or result > INT_MAX:
            return 0

        return result