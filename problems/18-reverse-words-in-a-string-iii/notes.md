# Notes

## Link
https://leetcode.com/problems/reverse-words-in-a-string-iii/

## Code
``` python
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(v[::-1]for v in s.split())
```

## Idea
- Key pattern(s): String
- Core steps:
    - Split string `s` and reverse members.
    - Combine all string members with `" "`.

## Complexity
- Time: O(n)
- Space: O(n)

## Gotcha
- I tried to code shorter.