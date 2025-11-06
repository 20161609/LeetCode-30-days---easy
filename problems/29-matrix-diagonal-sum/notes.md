# Notes

# Link
https://leetcode.com/problems/matrix-diagonal-sum/

## Code
``` python
from itertools import product
class Solution:
    def diagonalSum(self, m: List[List[int]]) -> int:
        return sum(m[y][x] for x,y in product(range(len(m)), range(len(m))) if y in (len(m)-1-x, x))
```

## Idea
- Key pattern(s): Using `itertools`s method(`product`).
- Core steps:
    - Gather all dots and collect dots on only diagonals.
    - Return sum of all dots' values.
    
## Complexity
- Time: O(n^2)
- Space: O(n^2)

## Review
- It's too difficult to code with a line..🤣`