# https://leetcode.com/problems/matrix-diagonal-sum/

from itertools import product
class Solution:
    def diagonalSum(self, m: List[List[int]]) -> int:
        return sum(m[y][x] for x,y in product(range(len(m)), range(len(m))) if y in (len(m)-1-x, x))
