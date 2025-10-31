# https://leetcode.com/problems/remove-element/description/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        return len(nums) - nums.count(val)