# Notes

## Link
https://leetcode.com/problems/balanced-binary-tree/description/

## Code
``` python
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
            if not node: return depth
            l, r = dfs(node.left, depth+1), dfs(node.right, depth+1)
            if abs(l-r) > 1: self.answer = False
            return max(l,r)
        dfs()
        return self.answer
```

## Idea
- Key pattern(s): Binary Tree, DFS search.
- Core steps:
    - DFS search and remember each node's the value which is max depth from current node.
    - Using global variable `self.answer`, I can return answer. Origin value is `True`, but it should be `False` when it meets that the difference between left's max depth and right's max depth is more that 1.

## Complexity
- Time: O(n)
- Space: O(n)

## Review
- Recursion code made it space comlexity with O(n). But I didn't come up with another way to calculate node's value that is max depth from current thing.