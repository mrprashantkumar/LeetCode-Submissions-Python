class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        visited = set()
        
        def dfs(node):
            cnt = 1
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    cnt += dfs(nei)
            return cnt
        
        ans = 0
        for i in range(n):
            if i not in visited:
                smans = dfs(i)
                if smans == n:
                    return 0
                else:
                    ans += smans*(n-smans)
        return ans//2