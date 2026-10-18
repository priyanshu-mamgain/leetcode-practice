from traitlets import List

class Solution:

    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        import sys
        sys.setrecursionlimit(10000)

        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD

        inv_fact = [1] * (n + 1)
        inv_fact[n] = pow(fact[n], MOD - 2, MOD)

        for i in range(n, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % MOD

        def comb(a, b):
            return fact[a] * inv_fact[b] % MOD * inv_fact[a - b] % MOD

        def dfs(arr):
            if len(arr) <= 2:
                return 1

            root = arr[0]
            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]

            left_ways = dfs(left)
            right_ways = dfs(right)

            interleavings = comb(len(arr) - 1, len(left))

            return interleavings * left_ways % MOD * right_ways % MOD

        return (dfs(nums) - 1) % MOD
