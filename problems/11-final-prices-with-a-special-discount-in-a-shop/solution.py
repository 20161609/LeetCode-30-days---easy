# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/

from collections import deque

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        queue = deque()
        for i, v in enumerate(prices):
            while queue and prices[queue[-1]] >= v:
                prices[queue.pop()] -= v
            queue.append(i)
        return prices