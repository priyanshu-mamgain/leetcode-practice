class Solution:
    def arrangeCoins(self, n: int) -> int:
        row = 1
        count = 0

        while n>= row :     
            n -= row        # n = Number of coins remaining.
            row += 1        # row = number of coins needed for current row.
            count += 1

        return count