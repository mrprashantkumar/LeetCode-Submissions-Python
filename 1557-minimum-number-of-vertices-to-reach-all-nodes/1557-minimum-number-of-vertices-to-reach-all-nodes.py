class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        
        for i, j in edges:
            graph[j].append(i)
        ans = []
        for i in range(n):
            if not graph[i]:
                ans.append(i)
        return ans