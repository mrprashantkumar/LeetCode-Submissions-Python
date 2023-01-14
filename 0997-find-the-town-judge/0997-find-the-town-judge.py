class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = [[] for _ in range(n+1)]
        
        for i, j in trust:
            graph[i].append(j)
        
        # print(graph)
        for i in range(1,n+1):
            if len(graph[i]) == 0 and all(i in graph[j] for j in range(1, n+1) if i != j):
                return i
        return -1