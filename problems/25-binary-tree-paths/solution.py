# https://leetcode.com/problems/binary-tree-paths/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        s = deque([(root, f'{root.val}')])
        answer = []
        while s:
            node, path = s.pop()
            if node.left == node.right: answer.append(path)            
            if node.left: s.append((node.left, f'{path}->{node.left.val}'))
            if node.right: s.append((node.right, f'{path}->{node.right.val}'))

        return answer