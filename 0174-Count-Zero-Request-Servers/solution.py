from typing import List

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda log: log[1])

        sorted_queries = sorted((q, i) for i, q in enumerate(queries))

        count = {}
        left = 0
        right = 0
        ans = [0] * len(queries)

        for q, idx in sorted_queries:
            start = q - x

            # Add logs whose time is <= query time
            while right < len(logs) and logs[right][1] <= q:
                server = logs[right][0]
                count[server] = count.get(server, 0) + 1
                right += 1

            # Remove logs older than the interval
            while left < right and logs[left][1] < start:
                server = logs[left][0]
                count[server] -= 1

                if count[server] == 0:
                    del count[server]

                left += 1

            # Servers with no requests = total - active servers
            ans[idx] = n - len(count)

        return ans