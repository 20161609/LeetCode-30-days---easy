# Notes

# https://leetcode.com/problems/binary-tree-paths/description/
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
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        s, answer = deque([(root, f'{root.val}')]), []
        while s:
            node, path = s.pop()
            if node.left == node.right: answer.append(path)            
            if node.left: s.append((node.left, f'{path}->{node.left.val}'))
            if node.right: s.append((node.right, f'{path}->{node.right.val}'))
        return answer
```
## Idea
- Key pattern(s): Binary Tree, DFS search
- Core steps:
    - Search all root with DFS and store the current path.
    - If the node is leaf, push the path to `answer`.

## Complexity
- Time: O(n)
- Space: O(n)

## Review
- How to figure out it's leaf node? -> Left is equal to Right.
- Max length of the path is 100.(It's explained in problem description), So I don't need to worry about path's size.