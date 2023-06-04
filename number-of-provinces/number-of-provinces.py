class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(node):
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)
        
        n = len(isConnected)
        graph = defaultdict(list)
        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j] == 1:
                    graph[i].append(j)
                    graph[j].append(i)

        visited = set()
        ans = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                ans += 1
        
        return ans