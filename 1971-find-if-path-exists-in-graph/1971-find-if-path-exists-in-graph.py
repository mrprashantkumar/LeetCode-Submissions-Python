class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        visited = set()
        qu = deque([source])
        visited.add(source)
        
        while qu:
            curr = qu.popleft()
            if curr == destination:
                return True
            
            for node in graph[curr]:
                if node not in visited:
                    visited.add(node)
                    qu.append(node)
        
        return False