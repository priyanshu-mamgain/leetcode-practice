class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        # Path length must be even
        if (m + n - 1) % 2 == 1:
            return False

        # First character must be '('
        if grid[0][0] == ')':
            return False

        # dp[i][j] = possible balances at (i, j)
        dp = [[set() for _ in range(n)] for _ in range(m)]

        dp[0][0].add(1)

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                previous_balances = set()

                # Come from above
                if i > 0:
                    previous_balances.update(dp[i - 1][j])

                # Come from left
                if j > 0:
                    previous_balances.update(dp[i][j - 1])

                for balance in previous_balances:
                    if grid[i][j] == '(':
                        new_balance = balance + 1
                    else:
                        new_balance = balance - 1

                    # Balance can never become negative
                    if new_balance >= 0:
                        dp[i][j].add(new_balance)

        return 0 in dp[m - 1][n - 1]