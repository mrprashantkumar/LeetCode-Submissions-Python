class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        indeg = [0]*n
        for x, y in roads:
            indeg[x] += 1
            indeg[y] += 1
        
        indeg.sort()
        ans = 0
        for value in range(1, n+1):
            ans += value * indeg[value-1]
        return ans