# Notes

## Link
https://leetcode.com/problems/isomorphic-strings/

## Code
``` python
from collections import defaultdict
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        m1, m2 = defaultdict(str), defaultdict(str)
        for x, y in zip(s, t):
            m1[x], m2[y] = (m1[x] if m1[x] else y), (m2[y] if m2[y] else x)            
            if m1[x] != y or m2[y] != x:
                return False
        return True
```

## Idea

* Check if characters in `s` and `t` map **one-to-one** consistently.
* Maintain two mappings: `s → t` and `t → s`.
* For each pair, ensure both directions match; otherwise return `False`.

## Complexity

* Time: O(n) — single pass through both strings.
* Space: O(k) — up to unique character count.

## Gotcha

* Must validate both mappings to avoid partial correspondence.
* Different lengths or inconsistent mapping immediately fail.
