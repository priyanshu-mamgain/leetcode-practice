from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # Coordinate compression
        values = sorted(set(nums))
        rank = {v: i + 1 for i, v in enumerate(values)}
        a = [rank[v] for v in nums]
        size = len(values)

        bit_c = [0] * (size + 1)
        bit_s = [0] * (size + 1)

        def update(i, dc, ds):
            while i <= size:
                bit_c[i] += dc
                bit_s[i] += ds
                i += i & -i

        def prefix(bit, i):
            res = 0
            while i:
                res += bit[i]
                i -= i & -i
            return res

        # Find the index of the kth smallest element
        def kth(kth_value):
            idx = 0
            step = 1 << (size.bit_length() - 1)

            while step:
                nxt = idx + step
                if nxt <= size and bit_c[nxt] < kth_value:
                    kth_value -= bit_c[nxt]
                    idx = nxt
                step >>= 1

            return idx + 1

        total_sum = 0

        # Initialize first window
        for i in range(x):
            update(a[i], 1, nums[i])
            total_sum += nums[i]

        def get_cost():
            mid_idx = kth((x + 1) // 2)
            mid = values[mid_idx - 1]

            left_count = prefix(bit_c, mid_idx)
            left_sum = prefix(bit_s, mid_idx)

            right_count = x - left_count
            right_sum = total_sum - left_sum

            return (
                mid * left_count - left_sum
                + right_sum - mid * right_count
            )

        costs = [get_cost()]

        # Sliding window
        for i in range(x, n):
            update(a[i - x], -1, -nums[i - x])
            total_sum -= nums[i - x]

            update(a[i], 1, nums[i])
            total_sum += nums[i]

            costs.append(get_cost())

        # DP: minimum cost to select exactly t windows
        INF = float('inf')
        prev = [0] * (n + 1)

        for t in range(1, k + 1):
            curr = [INF] * (n + 1)

            for i in range(x, n + 1):
                curr[i] = min(
                    curr[i - 1],
                    prev[i - x] + costs[i - x]
                )

            prev = curr

        return prev[n]