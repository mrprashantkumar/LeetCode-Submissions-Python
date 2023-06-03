class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        def dfs(node, parent):
            ans = 0
            for nei in graph[node]:
                if nei != parent:
                    ans = max(ans, dfs(nei, node))
            ans += informTime[node]
            return ans
        
        graph = defaultdict(list)
        for i in range(n):
            if manager[i] != -1:
                graph[manager[i]].append(i)
        return dfs(headID, -1)