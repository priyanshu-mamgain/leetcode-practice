class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        insert = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[insert], nums[i] = nums[i], nums[insert]
                insert += 1