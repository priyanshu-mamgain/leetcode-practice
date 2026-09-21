class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        result = [0] * k
        dp = [0] * k

        for num in nums:
            new_dp = [0] * k

            # Start a new subarray with just num
            remainder = num % k
            new_dp[remainder] += 1

            # Extend all previous subarrays
            for r in range(k):
                if dp[r] > 0:
                    new_remainder = (r * remainder) % k
                    new_dp[new_remainder] += dp[r]

            dp = new_dp

            # Add all subarrays ending at this position
            for r in range(k):
                result[r] += dp[r]

        return result