class Solution:
    def eventualSafeNodes(self, adj: List[List[int]]) -> List[int]:
        N = len(adj)
        graph = defaultdict(list)
        indeg = [0]*N
        for node in range(N):
            for nei in adj[node]:
                graph[nei].append(node)
                indeg[node] += 1
        
        qu = deque()
        for i in range(N):
            if indeg[i] == 0:
                qu.append(i)
        
        ans = []
        while qu:
            curr = qu.popleft()
            ans.append(curr)
            for nei in graph[curr]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    qu.append(nei)
        return sorted(ans)