class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        count = [1]*n
        ans = [0]*n
        
        def dfs(node, parent):
            for child in graph[node]:
                if child != parent:
                    dfs(child, node)
                    count[node] += count[child]
                    ans[node] += ans[child] + count[child]
        
        def dfs2(node, parent):
            for child in graph[node]:
                if child != parent:
                    ans[child] = ans[node] - count[child] + n - count[child]
                    dfs2(child, node)
        
        dfs(0, None)
        dfs2(0, None)
        
        return ans