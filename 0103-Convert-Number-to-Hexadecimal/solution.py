class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        digits = "0123456789abcdef"
        result = ""

        # Convert negative number to 32-bit two's complement
        if num < 0:
            num += 2 ** 32

        while num > 0:
            remainder = num % 16
            result += digits[remainder]
            num //= 16

        return result[::-1]