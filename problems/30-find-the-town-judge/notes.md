# Notes

## Link
https://leetcode.com/problems/find-the-town-judge/description/

## Code
``` python
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        box = {i+1: set() for i in range(n)}
        for a,b in trust: box[b].add(a)
        for a, _ in trust:
            if a in box: box.pop(a)
        if box:
            key, value = box.popitem()
            return key if len(value)==n-1 else -1
        return -1
```

## Idea
- Key pattern(s): Hash
- Core steps:
    - Declare dict `box`.(`{b1: {a1, a2, ...}, b2: {~~}}`).
        - a trust b.
    - Remove all indices which is trusting someone.
    - If there's no candidates, return `-1`.
    - Unique candidate should be trusted by all members with exception itself.

## Complexity
- Time: O(n)
- Space: O(n)

## Review
- Too many edges are included.. So it should be coded for safey code.(Never short liner..)