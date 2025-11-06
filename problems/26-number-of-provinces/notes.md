# Notes

## Link
https://leetcode.com/problems/number-of-provinces/

## Code
``` python
from collections import deque
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n,visited,queue = len(isConnected),set(),deque()
        answer = 0
        for node in range(n):
            if node in visited: continue
            queue.append(node), visited.add(node)
            answer+=1
            while queue:
                i = queue.popleft()
                for j in range(n):
                    if j in visited or isConnected[i][j]==0:continue
                    queue.append(j), visited.add(j)

        return answer
```

## Idea
- Key pattern(s): BFS search
- Core steps:
    - Iterating through 0 to the length of `isConnected`, each loop can begin from current node and visit all nodes connected with that.
    - If you visited that node, you don't need to consider the node.
    - Return the number of nodes which has been considered without visited.

## Complexity
- Time: O(n)
- Space: O(n)

## Review
- It can be optimized with using `Dict`. But it's too easy problem. So I didn't bother to add it.