# Notes

## Link
https://leetcode.com/problems/reshape-the-matrix/

## Code
``` python
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        H, W = len(mat), len(mat[0])
        if (r >= H and c >= W) or (r*c < H*W): return mat
        answer = [[0] * c for _ in range(r)]
        for y in range(H):
            for x in range(W):
                answer[(y*W+x)//c][(y*W+x)%c] = mat[y][x]
        return answer
```

## Idea
- Key pattern(s): Array.
- Core steps:
    - If you don't need to reshape the matrix, just return origin `mat`.
    - Decide each spot's order with `y * W + x` in `answer`.

## Complexity
- Time: O(n^2)
- Space: O(n^2)

## Gotcha
- It was very confusing to classify 2 indices `r` and `c`.
- Absolute order can be calculate with `x` and `y`.