class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        @cache
        def dfs(node):
            res = []
            for nei in graph[node]:
                res += dfs(nei)
            
            self.ans[node] = sorted(set(res))
            return self.ans[node] + [node]

        graph = defaultdict(list)
        indeg = [0]*n
        for x, y in edges:
            graph[y].append(x)
            indeg[x] += 1
        
        self.ans = [[] for _ in range(n)]
        for node in range(n):
            if indeg[node] == 0:
                dfs(node)
        return self.ans