# Notes

## Code
``` python
from collections import deque
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack, box = deque(), deque()
        for c in s:
            if not stack: box.append([])
            box[-1].append(c)
            if c == '(': stack.append(c)
            elif c == ')': stack.pop()
        return "".join(["".join(b[1:len(b)-1]) for b in box])
```

## Idea
- Key pattern(s): Use stack to store open parenthesis(`(`).
- Core steps:
    - Iterating through the string `s`.
    - In each loop, the code decides whether to pop or push and store the char into list `box`.
    - If a cycle of Parentheses has been closed, new cycle(`[]`) should be added to the list `box`.
    - Combine the strs that cut the front and back and return.    

## Complexity
- Time: O(n)
- Space: O(n)

## Gotcha
- I always come up with `stack` data structure first when I'm in front of the problem of `Parentheses`.