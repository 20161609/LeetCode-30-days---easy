# Notes

## Link
https://leetcode.com/problems/third-maximum-number/description/

## Code
``` python
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        if len(nums) < 3:
            return max(nums)

        nums.remove(max(nums)), nums.remove(max(nums))
        return max(nums)
```

## Idea

* Find the third distinct maximum value.
* Remove duplicates by converting the list to a set.
* If fewer than three distinct numbers exist, return the maximum.
* Otherwise, remove the top two maxima and return the next maximum.

## Complexity

* Time: O(n) — creating a set and finding/removing max values each once.
* Space: O(n) — storing unique elements in a set.

## Gotcha

* Order is lost when converting to a set.
* Must handle lists with fewer than three unique elements.
