class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        def dfs(node, prev):
            
            for child in graph[node]:
                if child != prev and dfs(child, node):
                    hasApple[node] = True
            return hasApple[node]

        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        dfs(0, -1)
        return (sum(hasApple) - hasApple[0]) * 2