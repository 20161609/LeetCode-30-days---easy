# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/description/

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum((len(str(num))+1)%2 for num in nums)
    