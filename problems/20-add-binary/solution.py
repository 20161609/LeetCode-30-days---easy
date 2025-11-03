# https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        y = sum([int(c)*2**i for i,c in enumerate(a[::-1])] + [int(c)*2**i for i,c in enumerate(b[::-1])])
        answer = []
        while y:
            answer.append(str(y%2))
            y //= 2

        return "".join(max(answer[::-1], ["0"]))