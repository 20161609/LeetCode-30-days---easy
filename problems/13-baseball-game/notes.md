# Notes

## Link
https://leetcode.com/problems/baseball-game/description/

## Code
``` python
from collections import deque
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = deque()
        for opr in operations:
            if opr == 'C': stack.pop()
            elif opr == 'D': stack.append(stack[-1] * 2)
            elif opr == '+': stack.append(stack[-1] + stack[-2])
            else: stack.append(int(opr))
        return sum(stack)
```

## Idea
- Key pattern(s): Use stack data structure to store numbers.
- Core steps:
    - Operation `C`: pop the top of `stack`. (The latest one)
    - Operation `D`: push the double of `stack`'s top.
    - Operation `+`: push the sum of `stack`'s top and next to the top.
    - Operation the others: Convert it to `int` and push it to `stack`.    

## Complexity
- Time: O(n)
- Space: O(n)

## Gotcha
- None..