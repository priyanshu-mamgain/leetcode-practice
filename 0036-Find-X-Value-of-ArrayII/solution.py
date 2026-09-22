
from typing import List


class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)

        # Each segment-tree node stores:
        # product = product of the whole segment modulo k
        # count[r] = number of non-empty prefixes
        #            whose product % k == r
        tree = [[1, [0] * k] for _ in range(2 * n)]

        def make_node(value):
            value %= k
            count = [0] * k
            count[value] = 1
            return [value, count]

        def merge(left, right):
            product_left, count_left = left
            product_right, count_right = right

            product = (product_left * product_right) % k
            count = count_left[:]

            # Prefix that enter the right segment
            # contain entire left segment first.
            for r in range(k):
                new_r = (product_left * r) % k
                count[new_r] += count_right[r]

            return [product, count]

        #leaves
        for i in range(n):
            tree[n + i] = make_node(nums[i])

        #tree
        for i in range(n - 1, 0, -1):
            tree[i] = merge(tree[2 * i], tree[2 * i + 1])

        def update(index, value):
            pos = n + index
            tree[pos] = make_node(value)

            pos //= 2

            while pos:
                tree[pos] = merge(tree[2 * pos], tree[2 * pos + 1])
                pos //= 2

        def query(left, right):
            # Query left, right
            left += n
            right += n

            left_node = [1, [0] * k]
            right_node = [1, [0] * k]

            while left <= right:
                if left % 2 == 1:
                    left_node = merge(left_node, tree[left])
                    left += 1

                if right % 2 == 0:
                    right_node = merge(tree[right], right_node)
                    right -= 1

                left //= 2
                right //= 2

            return merge(left_node, right_node)

        result = []

        for index, value, start, x in queries:
            update(index, value)

            _, count = query(start, n - 1)
            result.append(count[x])

        return result