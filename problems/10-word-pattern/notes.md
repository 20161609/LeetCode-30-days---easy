# Notes

## Link
https://leetcode.com/problems/word-pattern/

## Code
``` python
from collections import defaultdict
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        m1, m2 = defaultdict(str), defaultdict(str)
        for p, v in zip(pattern, s.split()):
            m1[p], m2[v] = (m1[p] if m1[p] else v), (m2[v] if m2[v] else p)
            if m1[p] != v or m2[v] != p:
                return False
        return len(pattern)==len(s.split())
```

## Idea

* Check if each character in `pattern` maps **one-to-one** with each word in `s`.
* Maintain two mappings:

  * `pattern → word`
  * `word → pattern`
* Iterate through both; if mismatch occurs, return `False`.
* Finally, ensure pattern length equals number of words.

## Complexity

* Time: O(n) — one pass through all characters/words.
* Space: O(k) — up to number of unique pattern–word pairs.

## Gotcha

* Length mismatch between pattern and words invalidates immediately.
* Must confirm bijective mapping (both directions match).
