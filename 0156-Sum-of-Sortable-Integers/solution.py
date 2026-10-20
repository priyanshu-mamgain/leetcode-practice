from typing import List

class Solution:
    def sortableIntegers(self, nums: List[int]) -> int:
        n = len(nums)
        sorted_nums = sorted(nums)
        answer = 0

        def is_rotation(block, target):
            k = len(block)
            doubled = block + block[:-1]

            # KMP prefix table for target
            lps = [0] * k
            j = 0

            for i in range(1, k):
                while j > 0 and target[i] != target[j]:
                    j = lps[j - 1]
                if target[i] == target[j]:
                    j += 1
                    lps[i] = j

            # Search target inside doubled
            j = 0
            for x in doubled:
                while j > 0 and x != target[j]:
                    j = lps[j - 1]
                if x == target[j]:
                    j += 1
                if j == k:
                    return True

            return False

        for k in range(1, n + 1):
            if n % k != 0:
                continue

            valid = True

            for start in range(0, n, k):
                block = nums[start:start + k]
                target = sorted_nums[start:start + k]

                if not is_rotation(block, target):
                    valid = False
                    break

            if valid:
                answer += k

        return answer
