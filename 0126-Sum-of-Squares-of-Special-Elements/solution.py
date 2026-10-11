
from typing import List

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        
        total = 0
        n = len(nums)

        for i in range(len(nums)):
            if n % (i + 1) == 0:            
                total += nums[i] * nums[i]

        return total 