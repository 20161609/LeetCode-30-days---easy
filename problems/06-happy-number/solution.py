# https://leetcode.com/problems/happy-number/

class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set([n])
        while n != 1:
            n = sum(int(x)**2 for x in str(n))
            if n in visited:
                return False
            visited.add(n)
        return True