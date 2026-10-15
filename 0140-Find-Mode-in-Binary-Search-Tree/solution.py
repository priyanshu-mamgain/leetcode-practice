# Definition for a binary tree node.

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        count = {}

        def dfs(node):
            if node is None:
                return

            count[node.val] = count.get(node.val, 0) + 1

            dfs(node.left)
            dfs(node.right)

        dfs(root)

        max_count = max(count.values())
        result = []

        for value, frequency in count.items():
            if frequency == max_count:
                result.append(value)

        return result
