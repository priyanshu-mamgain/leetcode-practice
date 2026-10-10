class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        n = len(nums1)
        k = k1 + k2

        diff = []
        for i in range(n):
            diff.append(abs(nums1[i] - nums2[i]))

        # If we can remove every difference, the answer is 0
        if sum(diff) <= k:
            return 0

        # Sort differences from largest to smallest
        diff.sort(reverse=True)

        for i in range(n):
            next_diff = diff[i + 1] if i + 1 < n else 0
            count = i + 1

            # Operations needed to lower the largest differences
            needed = (diff[i] - next_diff) * count

            if k >= needed:
                k -= needed
            else:
                # Spread the remaining operations evenly
                level = diff[i] - k // count
                remainder = k % count

                answer = 0

                # Some differences become level - 1
                answer += remainder * (level - 1) ** 2

                # The others remain at level
                answer += (count - remainder) * level ** 2

                # Add squares of differences not yet included
                for j in range(i + 1, n):
                    answer += diff[j] ** 2

                return answer

        return 0