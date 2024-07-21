class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def getTopoSort(k, conditions):
            graph = defaultdict(list)
            indegree = [0] * (k + 1)
            
            for u, v in conditions:
                graph[u].append(v)
                indegree[v] += 1
            
            qu = deque([i for i in range(1, k + 1) if indegree[i] == 0])
            order = []
            
            while qu:
                node = qu.popleft()
                order.append(node)
                for neighbor in graph[node]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        qu.append(neighbor)
            
            if len(order) != k:
                return [] 
            return order
        
        rows = getTopoSort(k, rowConditions)
        cols = getTopoSort(k, colConditions)
        
        if not rows or not cols:
            return []
        
        rowPosition = {num: i for i, num in enumerate(rows)}
        colPosition = {num: i for i, num in enumerate(cols)}
        
        ans = [[0]*k for _ in range(k)]
        
        for num in range(1, k + 1):
            r, c = rowPosition[num], colPosition[num]
            ans[r][c] = num
        
        return ans