# https://leetcode.com/problems/reshape-the-matrix/

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        H, W = len(mat), len(mat[0])
        if (r >= H and c >= W) or (r*c < H*W):
            return mat

        answer = [[0] * c for _ in range(r)]
        for y in range(H):
            for x in range(W):
                answer[(y*W+x)//c][(y*W+x)%c] = mat[y][x]
        return answer