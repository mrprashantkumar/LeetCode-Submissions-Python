class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def helper(node):
            for i, child in enumerate(isConnected[node]):
                if child and i not in visited:
                    visited.add(i)
                    helper(i)
            
            
        n = len(isConnected)
        visited = set()
        ans = 0
        for i in range(n):
            if i not in visited:
                visited.add(i)
                helper(i)
                ans += 1
        return ans