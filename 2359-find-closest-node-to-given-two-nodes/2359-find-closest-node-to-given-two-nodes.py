class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def dfs(node, seen , counter=0):
            seen[node] = counter
            adj = edges[node]
            if adj != -1 and seen[adj] == -1 : 
                dfs(adj, seen, counter+1)
            return seen
        
        n = len(edges)
        
        seen1 = [-1]*n
        dfs(node1,seen1)

        seen2 = [-1]*n
        dfs(node2,seen2)

        maxDist = float("inf")
        res = -1
        for i in range(n) :
            if seen1[i] != -1 and seen2[i] != -1 :
                currMaxDist = max(seen1[i],seen2[i])
                if currMaxDist < maxDist :
                    res = i
                    maxDist = currMaxDist
        return res