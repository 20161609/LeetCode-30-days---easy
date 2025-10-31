# https://leetcode.com/problems/isomorphic-strings/
from collections import defaultdict

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        m1, m2 = defaultdict(str), defaultdict(str)
        for x, y in zip(s, t):
            m1[x], m2[y] = (m1[x] if m1[x] else y), (m2[y] if m2[y] else x)            
            if m1[x] != y or m2[y] != x:
                return False
        return True