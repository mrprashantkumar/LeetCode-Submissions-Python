class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        def dfs(node):
            nonlocal ans
            if node not in seen:
                if node in vis:
                    ans = max(ans,len(vis) - vis[node])
                elif edges[node] != -1:
                    vis[node] = len(vis)
                    dfs(edges[node])
                    vis.pop(node)
                seen[node] = True
        
        ans = -1
        seen = {}
        vis = {}
        for i in range(len(edges)):
            dfs(i)
        return ans