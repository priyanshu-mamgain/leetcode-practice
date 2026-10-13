
from collections import defaultdict, deque
from typing import List

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)

        if n == 1:
            return 0

        positions = defaultdict(list)

        for i, num in enumerate(arr):
            positions[num].append(i)

        queue = deque([(0, 0)])
        visited = {0}

        while queue:
            i, steps = queue.popleft()

            if i == n - 1:
                return steps

            next_indices = [i - 1, i + 1]
            next_indices.extend(positions[arr[i]])

            for j in next_indices:
                if 0 <= j < n and j not in visited:
                    visited.add(j)
                    queue.append((j, steps + 1))

            positions[arr[i]].clear()

        return -1