class Solution:
    def findComplement(self, num: int) -> int:

        bit = num.bit_length()          # Count Binary Length of Num
        mask = (1 << bit) - 1           # Mask is a number we use to control or change specific bits of another number.
        return num ^ mask