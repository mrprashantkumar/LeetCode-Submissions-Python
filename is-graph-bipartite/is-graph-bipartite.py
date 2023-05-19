class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n, colored = len(graph), {}
        for i in range(n):
            if i not in colored and graph[i]:
                colored[i] = 1
                qu = deque([i])
                while qu:
                    cur = qu.popleft()
                    for nei in graph[cur]:
                        if nei not in colored:
                            colored[nei] = -colored[cur]
                            qu.append(nei)
                        elif colored[nei] == colored[cur]:
                            return False
        return True