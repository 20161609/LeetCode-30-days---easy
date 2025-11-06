# Notes

# Link
https://leetcode.com/problems/find-center-of-star-graph/description/

## Code
``` python
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        return (set(edges[0])&set(edges[1])).pop()
```

## Idea
- Key pattern(s): Method `set`
- Core steps:
    - Using `set`, it can get intersection between `edges[0]` and `edges[1]`. And just return it.

## Complexity
- Time: O(1)
- Space: O(1)

## Review
- All edges are including star's node. So you don't have to consider all nodes.