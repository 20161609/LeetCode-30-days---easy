# Notes

## Link
https://leetcode.com/problems/remove-element/description/

## Code
``` python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        return len(nums) - nums.count(val)
```

## Idea

* **Key pattern(s):** In-place removal using two-pointer technique.
* **Core steps:**

  * Keep a write pointer for the next valid position.
  * Iterate through `nums`; copy elements not equal to `val`.
  * Return the new length.

## Complexity

* **Time:** O(n)
* **Space:** O(1)

## Gotcha

* Elements beyond the returned length are ignored.
* Order of remaining elements can change depending on approach.
