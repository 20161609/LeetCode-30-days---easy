# Notes

## Link
https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/description/

## Code
``` python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        return (max(nums)-1)*(max(v for i,v in enumerate(nums) if i!=nums.index(max(nums)))-1)

```

## Idea

* **Key pattern(s):** Find the two largest numbers in the list, then compute `(a−1)*(b−1)`.
* **Core steps:**

  * Identify the maximum element in `nums`.
  * Find the second-largest element (excluding the first max’s index).
  * Subtract 1 from both and multiply the results.

## Complexity

* **Time:** O(n) — both `max()` operations traverse the list once.
* **Space:** O(1) — only a few variables stored.

## Gotcha

* Using `max()` twice results in two full passes over the list.
* Ties for the maximum value are handled safely since indices are checked.
