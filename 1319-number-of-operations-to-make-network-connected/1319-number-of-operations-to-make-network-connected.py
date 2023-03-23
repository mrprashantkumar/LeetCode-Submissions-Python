class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        
        graph = [set() for i in range(n)]
        for i, j in connections:
            graph[i].add(j)
            graph[j].add(i)
        seen = [0] * n

        def dfs(i):
            if seen[i]:
                return 0
            seen[i] = 1
            for j in graph[i]:
                dfs(j)
            return 1

        return sum(dfs(i) for i in range(n)) - 1