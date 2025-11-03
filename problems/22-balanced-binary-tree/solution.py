# https://leetcode.com/problems/balanced-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.answer = True
        def dfs(node=root, depth=0):
            if not node:
                return depth
            l, r = dfs(node.left, depth+1), dfs(node.right, depth+1)
            if abs(l-r) > 1:
                self.answer = False
            return max(l,r)
        dfs()
        return self.answer