class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        ans = [[] for _ in range(n+1)]
        ans[1].append(0)
        qu = [(0, 1)]
        while qu:
            minDist, node = heappop(qu)
            if node == n and len(ans[n]) == 2:
                return max(ans[n])
            
            for nei in graph[node]:
                if (minDist // change) % 2 == 0:
                    val = minDist + time
                else:
                    val = ceil(minDist / (2 * change)) * (2 * change) + time
                
                if not ans[nei] or (len(ans[nei]) == 1 and ans[nei][0] != val):
                    ans[nei].append(val)
                    heappush(qu, (val, nei))
