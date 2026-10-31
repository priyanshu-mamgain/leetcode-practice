from typing import List

class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7

        n = len(grid[0])
        down = [1] + [0] * (n - 1)

        for row in grid:
            right = 0

            for j in range(n):
                if row[j] == 1:
                    # Mirror: swap the incoming directions
                    right, down[j] = down[j], right

                else:
                    # Empty cell: both incoming paths can continue
                    right = (right + down[j]) % MOD
                    down[j] = right

        return right