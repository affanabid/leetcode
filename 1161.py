from typing import Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        i, level, mx, q = 0, 0, -float('inf'), deque()
        q.append(root)
        while q:
            curr = 0
            for _ in range(len(q)):
                node = q.popleft()
                curr += node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                print('Curr: ', curr, 'Max: ', mx)
            if curr > mx:
                mx = curr
                level = i
            i += 1
        return level + 1
    

root = TreeNode(-100)
root.left = TreeNode(-200)
root.right = TreeNode(-300)
root.left.left = TreeNode(-20)
root.left.right = TreeNode(-5)
root.right.left = TreeNode(-10)

sol = Solution()
print(sol.maxLevelSum(root))