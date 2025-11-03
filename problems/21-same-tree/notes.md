# Notes

# Link
https://leetcode.com/problems/same-tree/description/

## Code
``` python
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque([(p,q)])
        while queue:
            p, q = queue.popleft()
            if bool(p)^bool(q): return False
            elif p == None: continue
            elif p.val != q.val: return False
            queue.append((p.left, q.left)), queue.append((p.right, q.right))
        return True
```

## Idea
- Key pattern(s): BFA search, Tree Structure.
- Core steps:
    - Search all with BFS.
    - Where should I stop and return `False`?
        1. One is not `Null`, but the other is `Null`.
        2. Both values of them are different each other.

## Complexity
- Time: O(n)
- Space: O(n)

## Review
- Using xor(`^`), it can be coded easily.