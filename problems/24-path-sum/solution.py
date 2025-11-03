# https://leetcode.com/problems/path-sum/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        s = deque() # stack
        if root:
            s.append([root, root.val])
        else:
            return False
        while s:
            node, _sum = s.pop()
            if (node.left == node.right == None) and (_sum == targetSum):
                return True
            if node.left:s.append([node.left, _sum+node.left.val])
            if node.right:s.append([node.right, _sum+node.right.val])
        return False