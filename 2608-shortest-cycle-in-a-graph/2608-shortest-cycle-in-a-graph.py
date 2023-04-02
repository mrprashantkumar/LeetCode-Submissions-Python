class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        ans = 1000000007
        for i in range(n):
            qu = deque([i])
            dist = [-1]*n
            dist[i] = 0

            while qu:
                node = qu.popleft()
                for nei in graph[node]:
                    if dist[nei] == -1:
                        dist[nei] = dist[node] + 1
                        qu.append(nei)
                    elif dist[nei] >= dist[node]:
                        ans = min(ans, dist[node] + dist[nei] + 1)

        if ans == 1000000007:
            return -1 
        else:
            return ans