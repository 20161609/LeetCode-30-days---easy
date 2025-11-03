# Notes

## Link
https://leetcode.com/problems/path-sum/description/

## Code
``` python
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
        if not root: return False
        s.append([root, root.val])
        while s:
            node, _sum = s.pop()
            if (node.left == node.right == None) and (_sum == targetSum):return True
            if node.left:s.append([node.left, _sum+node.left.val])
            if node.right:s.append([node.right, _sum+node.right.val])
        return False
```

## Idea
- Key pattern(s): DFS search, Binary Tree
- Core steps:
    - Search all nodes with DFS
    - If you find the leaf and the `_sum` is same with `targetSum`, return `True`.
    - There's no leaf which has `_sum`==`targetSum`, return `False`.

## Complexity
- Time: O(n)
- Space: O(n)

## Gotcha
- DFS search makes it faster to approach leaf node.