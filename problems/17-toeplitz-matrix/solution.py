# https://leetcode.com/problems/toeplitz-matrix/description/

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