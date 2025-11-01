# Notes  

## Link  
https://leetcode.com/problems/valid-sudoku/description/  

## Code
``` python
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
```

## Idea  
- Validate a 9×9 Sudoku board ensuring no duplicates in:  
  - Each row  
  - Each column  
  - Each 3×3 sub-box  
- Skip cells containing `'.'`.  
- For each filled cell, check that its value appears only once in its row, column, and box.  

## Complexity  
- Time: O(9^2) — every cell checked with constant-size scans.  
- Space: O(1) — uses only temporary counters per iteration.  

## Gotcha  
- Counting via `.count()` re-traverses rows/columns/boxes → less efficient but simple.  
- Must handle `'.'` as an empty cell and ignore it in checks.