# Notes

## Link
https://leetcode.com/problems/two-out-of-three/description/

## Code
``` python
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        s1 ,s2 ,s3 = set(nums1), set(nums2), set(nums3)
        return list((s1&s2)|(s2&s3)|(s3&s1))
```

## Idea

* Find numbers that appear in at least **two** of the three lists.
* Convert each list to a set to remove duplicates.
* Use set intersection and union to combine elements present in two or more sets:
  `(s1 & s2) | (s2 & s3) | (s3 & s1)`.

## Complexity

* Time: O(n) — each list is processed once, and set operations are linear in total elements.
* Space: O(n) — sets store unique elements from all lists.

## Gotcha

* Input lists may contain duplicates; converting to sets handles that.
* Order of the returned list is arbitrary since sets are unordered.
