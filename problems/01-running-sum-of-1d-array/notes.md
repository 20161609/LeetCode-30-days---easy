# Notes

## Link
https://leetcode.com/problems/running-sum-of-1d-array/

## Code
``` python
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(1, n):
            nums[i] += nums[i-1]
        return nums
```

## Idea

* Compute the cumulative sum as we iterate through the array.
* Update each element in place: `nums[i] = nums[i] + nums[i - 1]`.

## Complexity

* **Time:** O(n) — single pass through the list.
* **Space:** O(1) — updates are done in place, no extra space used.

## Gotcha

* The input list `nums` is modified in place.
* Must start from index `1` to avoid out-of-range access.

