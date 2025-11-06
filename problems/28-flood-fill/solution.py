# https://leetcode.com/problems/flood-fill/
from itertools import product
from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        H, W = len(image), len(image[0])
        queue,flood,image[sr][sc] = deque([(sr, sc)]),image[sr][sc],'-'
        while queue:
            r, c = queue.popleft()
            for nr, nc in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                if not(0<=nr<H and 0<=nc<W) or image[nr][nc] != flood:
                    continue
                image[nr][nc]='-'
                queue.append((nr,nc))
        for x,y in product(range(W), range(H)): 
            image[y][x] = color if image[y][x]=='-' else image[y][x]
        return image