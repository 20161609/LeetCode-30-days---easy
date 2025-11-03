# Notes

## Link
https://leetcode.com/problems/minimum-depth-of-binary-tree/

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
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None: return 0
        q = deque([(root, 1)])
        while q:
            node, path = q.popleft()
            if node.left == node.right == None: return path
            if node.left: q.append((node.left, path+1))
            if node.right: q.append((node.right, path+1))
```

## Idea
- Key pattern(s): BFS search, Binary Tree
- Core steps:
    - Searching nodes with BFS, It can get the shortest path.
    - Edge case(When root is `Null`) -> return 0.

## Complexity
- Time: O(n)
- Space: O(n)

## Review
- If you use DFS, the return value may not be the shortest one.