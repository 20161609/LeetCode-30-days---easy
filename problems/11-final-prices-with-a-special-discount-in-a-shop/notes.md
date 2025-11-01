# Notes

## Link

https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/

## Code
``` python
from collections import deque
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        queue = deque()
        for i, v in enumerate(prices):
            while queue and prices[queue[-1]] >= v:
                prices[queue.pop()] -= v
            queue.append(i)
        return prices
```

## Idea

* Key pattern(s): Use a **monotonic stack** to find for each price the next cheaper or equal price to its right.
* Core steps:

  * Maintain a stack of indices of items yet to receive their discount.
  * Iterate over each index (i); while the stack isn’t empty and `prices[stack[-1]] >= prices[i]`, pop the index and subtract `prices[i]` from `prices[pop_index]`.
  * Push `i` onto the stack.
  * Return the modified `prices` array.

## Complexity

* Time: O(n) — each index is pushed/popped at most once thanks to the stack.
* Space: O(n) — in worst case the stack may hold all indices.
## Gotcha

* You must check `>=` (not just `>`) because “less than or equal” qualifies for discount. ([DEV Community][3])
* You modify the same `prices` array in place; ensure you subtract the discount only once per applicable item.