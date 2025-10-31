# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/description/

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        return (max(nums)-1) * (max(v for i, v in enumerate(nums) if i != nums.index(max(nums)))-1)
