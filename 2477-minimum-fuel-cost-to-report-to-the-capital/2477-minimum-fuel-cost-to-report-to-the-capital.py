class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        n = len(roads)+1
        graph = [[] for i in range(n)]
        parent = [0]*n
        for i, j in roads:
            graph[i].append(j)
            graph[j].append(i)
        
        dist = [-1]*n
        q = deque([0])
        dist[0] = 0

        order = []
        while q:
            cur = q.popleft()
            for i in graph[cur]:
                if dist[i] == -1:
                    if i:
                        order.append(i)
                    parent[i] = cur
                    dist[i] = dist[cur]+1
                    q.append(i)
                    
        
        ans = 0
        cur = [1] * n
        for i in order[::-1]:
            ans += (cur[i]+seats-1)//seats 
            cur[parent[i]] += cur[i]
            
        return ans