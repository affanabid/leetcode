from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def checker(node, max_val):
            if not node:
                return 0
            if node.val >= max_val:
                max_val = node.val
                return checker(node.left, max_val) + checker(node.right, max_val) + 1
            return checker(node.left, max_val) + checker(node.right, max_val)
        return checker(root.left, root.val) + checker(root.right, root.val) + 1  