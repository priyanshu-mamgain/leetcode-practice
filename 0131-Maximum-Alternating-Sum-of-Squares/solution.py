
from traitlets import List

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        squares = sorted([x * x for x in nums])

        n = len(nums)
        half = n // 2

        return sum(squares[half:]) - sum(squares[:half])