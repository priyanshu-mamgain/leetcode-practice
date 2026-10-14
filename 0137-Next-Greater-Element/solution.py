from traitlets import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []

        for num in nums1:
            index = nums2.index(num)
            next_greater = -1

            for j in range(index + 1, len(nums2)):
                if nums2[j] > num:
                    next_greater = nums2[j]
                    break

            ans.append(next_greater)

        return ans