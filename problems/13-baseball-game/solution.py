# https://leetcode.com/problems/baseball-game/description/

from collections import deque

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = deque()
        for opr in operations:
            if opr == 'C':
                stack.pop()
            elif opr == 'D':
                stack.append(stack[-1] * 2)
            elif opr == '+':
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(opr))
        return sum(stack)