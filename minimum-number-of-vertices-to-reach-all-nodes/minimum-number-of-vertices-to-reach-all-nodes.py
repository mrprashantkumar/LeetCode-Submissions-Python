class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indeg = [0]*n
        for i, j in edges:
            indeg[j] += 1
        ans = []
        for i in range(n):
            if indeg[i] == 0:
                ans.append(i)
        return ans