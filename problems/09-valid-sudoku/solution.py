# https://leetcode.com/problems/valid-sudoku/description/

from itertools import product

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for y in range(9):
            for x in range(9):
                v = '' if board[y][x] == '.' else board[y][x]
                if board[y].count(v)>1:
                    return False
                if [board[i][x] for i in range(9)].count(v)>1:
                    return False
                if [board[i][j] for j,i in product(range(x-x%3,x-x%3+3),range(y-y%3,y-y%3+3))].count(v)>1:
                    return False                    
        return True