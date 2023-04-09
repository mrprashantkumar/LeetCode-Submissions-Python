class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        graph = defaultdict(list)
        indeg = [0]*n
        for i, j in edges:
            graph[i].append(j)
            indeg[j] += 1
        
        dp = [[0]*26 for _ in range(n)]
        qu = deque()
        for i in range(n):
            if indeg[i] == 0:
                qu.append(i)
        
        ans = 0
        visited = 0
        while qu:
            curr = qu.popleft()
            dp[curr][ord(colors[curr])-97] += 1
            ans = max(ans, dp[curr][ord(colors[curr])-97])
            visited += 1
            
            for nei in graph[curr]:
                for i in range(26):
                    dp[nei][i] = max(dp[nei][i], dp[curr][i])
                    
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    qu.append(nei)

        return ans if visited == n else -1