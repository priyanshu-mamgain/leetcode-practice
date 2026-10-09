class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:

        perimeter = 0       # Initial Value

        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if grid[i][j] == 1:                   # On-Land Box
                    perimeter += 4

                    if j > 0 and grid[i][j - 1] == 1:       # Left Box
                        perimeter -= 2

                    if i > 0 and grid[i - 1][j] == 1:       # Top Box
                        perimeter -= 2

        return perimeter 