from typing import List

class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        k = -1

        for i in range(n):
            if nums[i] != i:
                k &= nums[i]

        return max(k, 0)
