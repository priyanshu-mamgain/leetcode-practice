class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        
        first=float("-inf")
        second=float("-inf")
        third=float("-inf")

        for num in nums:

            if num == first or num == second or num == third:
                continue

            elif num > first:
                first, second, third = num, first, second
                
            elif num > second:
                first, second, third = first, num, second

            elif num > third:
                first, second, third = first, second, num

        if third == float("-inf"):
            return first
        else:
            return third

        