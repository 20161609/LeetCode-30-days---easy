# https://leetcode.com/problems/backspace-string-compare/

from collections import deque
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stk1, stk2 = deque(), deque()
        for c in s:
            if c != '#': stk1.append(c)
            elif stk1: stk1.pop()
        for c in t:
            if c != '#': stk2.append(c)
            elif stk2: stk2.pop()
        return "".join(stk1) == "".join(stk2)