# Notes

## Link
https://leetcode.com/problems/implement-stack-using-queues/

## Code
``` python
from collections import deque
class MyStack:
    def __init__(self): self.stack = deque()
    def push(self, x: int) -> None: self.stack.append(x)
    def pop(self) -> int: return self.stack.pop()
    def top(self) -> int: return self.stack[-1]
    def empty(self) -> bool: return len(self.stack) == 0
```

## Idea
- Key pattern(s): Stack
- Just use method(`collections`)'s `deque`.

## Complexity
- Time: O(-)
- Space: O(-)

## Gotcha
- There's nothing to talk about.