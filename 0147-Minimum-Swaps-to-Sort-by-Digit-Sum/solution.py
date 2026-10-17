from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        
        def digit_sum(num):
            total = 0
            while num > 0:
                total += num % 10
                num //= 10
            return total

        sorted_nums = sorted(nums, key=lambda x: (digit_sum(x), x))

        target_index = {num: i for i, num in enumerate(sorted_nums)}

        visited = [False] * len(nums)
        swaps = 0

        for i in range(len(nums)):
            if visited[i] or target_index[nums[i]] == i:
                continue

            cycle_length = 0
            j = i

            while not visited[j]:
                visited[j] = True
                j = target_index[nums[j]]
                cycle_length += 1

            swaps += cycle_length - 1

        return swaps