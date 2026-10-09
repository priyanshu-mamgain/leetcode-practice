class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        result = (x^y).bit_count()    # ^ = Bitwise XOR, ().bit_count() = Built-in operation(Python) to count number of Bits.
        return result
