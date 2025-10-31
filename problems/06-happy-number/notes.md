# Notes

## Link
https://leetcode.com/problems/happy-number/

## Code
``` python
# https://leetcode.com/problems/happy-number/

class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set([n])
        while n != 1:
            n = sum(int(x)**2 for x in str(n))
            if n in visited:
                return False
            visited.add(n)
        return True
```

## Idea

* Use cycle detection to check if repeatedly summing the squares of digits reaches 1.
* Track seen numbers in a set to detect infinite loops.
* If `n` becomes 1 → happy number; if a repeat occurs → not happy.

## Complexity

* Time: O(log n) — each transformation reduces the number’s magnitude roughly to the sum of squared digits.
* Space: O(log n) — stores previously seen numbers.

## Gotcha

* Must detect cycles; otherwise loop runs infinitely.
* Converting to string each time adds small overhead but keeps code simple.
