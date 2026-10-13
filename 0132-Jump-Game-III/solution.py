class Solution:
    def canReach(self, arr: list[int], start: int) -> bool:
        visited = set()
        stack = [start]

        while stack:
            i = stack.pop()

            if arr[i] == 0:
                return True

            if i in visited:
                continue

            visited.add(i)

            left = i - arr[i]
            right = i + arr[i]

            if left >= 0:
                stack.append(left)

            if right < len(arr):
                stack.append(right)

        return False