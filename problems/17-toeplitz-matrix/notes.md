# Notes

## Link
https://leetcode.com/problems/toeplitz-matrix/description/

## Code
``` python
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        H, W = len(matrix), len(matrix[0])
        for x in range(W):
            tmp, y = matrix[0][x], 0
            while x<W and y<H:
                if matrix[y][x] != tmp:
                    return False
                x, y = x+1, y+1
        
        for y in range(H):
            tmp, x = matrix[y][0], 0
            while x<W and y<H:
                if matrix[y][x] != tmp:
                    return False
                x, y = x+1, y+1
        
        return True
```

## Idea
- Key pattern(s): Array
- Core steps:
    - Iterating two line, one is all set of spots which has `x = 0`, and the other one is with `y = 0`.
    - Each loop, the spot should shift to bottom-right until the `matrix`s size.


## Complexity
- Time: O(n^2)
- Space: O(1)

## Gotcha
- Nothing to say.