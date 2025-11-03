# Notes

## Link
https://leetcode.com/problems/add-binary/

## Code
``` python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        y = sum([int(c)*2**i for i,c in enumerate(a[::-1])]+[int(c)*2**i for i,c in enumerate(b[::-1])])
        answer = []
        while y:
            answer.append(str(y%2))
            y //= 2
        return "".join(max(answer[::-1], ["0"]))
```

## Idea
- Key pattern(s): String, Binary(Math)
- Core steps:
    - Convert both `a` and `b` to `int`. and get sum of both.
    - Convert sum to binary. and return it with `str`.
    - Edge case: If the sum is Zero(`0`), replace the answer to (`["0"]`).

## Complexity
- Time: O(n)
- Space: O(n)

## Review
- Effort to get shorter code makes me feeling a few burden.. But satisfied. I think it's a Python's merit.