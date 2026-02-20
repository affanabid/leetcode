from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def checker(node, leaves):
            if not node.left and not node.right:
                leaves.append(node.val)
                return leaves
            if node.left:
                leaves = checker(node.left, leaves)
            if node.right:
                leaves = checker(node.right, leaves)
            return leaves
        leaves1, leaves2 = [], []
        leaves1 = checker(root1, leaves1)
        leaves2 = checker(root2, leaves2)
        return leaves1 == leaves2