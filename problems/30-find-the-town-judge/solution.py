# https://leetcode.com/problems/find-the-town-judge/description/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        box = {i+1: set() for i in range(n)}
        for a,b in trust: box[b].add(a)
        for a, _ in trust:
            if a in box: box.pop(a)
        if box:
            key, value = box.popitem()
            return key if len(value)==n-1 else -1
        return -1