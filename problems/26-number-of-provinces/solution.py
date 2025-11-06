# https://leetcode.com/problems/number-of-provinces/

from collections import deque
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited, queue = set(), deque()
        answer = 0
        for node in range(n):
            if node in visited:
                continue
            queue.append(node), visited.add(node)
            answer+=1
            while queue:
                node = queue.popleft()
                for nxt in range(n):
                    if nxt in visited or isConnected[nxt][node]==0:
                        continue
                    queue.append(nxt), visited.add(nxt)

        return answer