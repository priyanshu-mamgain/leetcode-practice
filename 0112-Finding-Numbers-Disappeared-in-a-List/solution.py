class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:

        result = []

        for num in nums:

            if nums[abs(num) - 1] > 0:                        # index = num - 1
                nums[abs(num) - 1] = -nums[abs(num) - 1]      # Marking Present

        for i in range(len(nums)):

            if nums[i] > 0:
                result.append(i+1)
        
        return result
