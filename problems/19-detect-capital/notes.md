# Notes

## Link
https://leetcode.com/problems/detect-capital/

## Code
``` python
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return len(word)==1 or word.isupper() or word[1:].islower()
    
```

## Idea
- Key pattern(s): String method
- Core steps:
    - If the length of word is 1, just return `True`.
    - If all characters are upper, then it can satisfies the first condition.
    - If all characters in `word[1:]` are all lower(), you don't need to `word[0]`. Because it has satisfied already second, third conditions.

## Complexity
- Time: O(n)
- Space: O(n)

## Review
- This is my just favorite code style. I'd love to get shorter one. Even if it has the lower efficiency, a computer which has good perfomance can resolve it.🤣