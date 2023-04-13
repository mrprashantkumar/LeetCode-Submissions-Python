class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        edges = len(connections)
        if edges < n-1:
            return -1
        
        def dfs(node):
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)
        
        graph = defaultdict(list)
        for i, j in connections:
            graph[i].append(j)
            graph[j].append(i)
        
        ans = 0
        visited = set()
        for i in range(n):
            if i not in visited:
                dfs(i)
                ans += 1
        
        return ans-1