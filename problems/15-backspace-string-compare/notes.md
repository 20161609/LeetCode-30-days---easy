# Notes

## Link
https://leetcode.com/problems/backspace-string-compare/

## Code
``` python
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
```

## Idea
- Key pattern(s): Use `stack` to store characters from `s` and `t`.
- Core steps:
    - when backspace(`#`), it must pop each `stack`.
    - Other characters are just pushed to the `stack`.

## Complexity
- Time: O(n)
- Space: O(n)

## Gotcha
- There was a trap.. When the `stack` is empty, `pop` can cause an error.