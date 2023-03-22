class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(dict)
        for u, v, w in roads:
            graph[u][v] = w
            graph[v][u] = w
        
        ans = 1000000007
        visited = set()
        qu = deque([1])

        while qu:
            node = qu.popleft()
            for adj, scr in graph[node].items():
                if adj not in visited:
                    qu.append(adj)
                    visited.add(adj)
                ans = min(ans,scr)
                
        return ans