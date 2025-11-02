# https://leetcode.com/problems/remove-outermost-parentheses/

from collections import deque
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack, box = deque(), deque()
        for c in s:
            if not stack:
                box.append([])

            box[-1].append(c)
            if c == '(':
                stack.append(c)
            elif c == ')':
                stack.pop()

        return "".join(["".join(b[1:len(b)-1]) for b in box])
