# https://leetcode.com/problems/word-pattern/

from collections import defaultdict
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        m1, m2 = defaultdict(str), defaultdict(str)
        for p, v in zip(pattern, s.split()):
            m1[p], m2[v] = (m1[p] if m1[p] else v), (m2[v] if m2[v] else p)
            if m1[p] != v or m2[v] != p:
                return False
        return len(pattern)==len(s.split())
    