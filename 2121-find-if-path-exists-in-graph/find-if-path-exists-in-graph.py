class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def dfs(node, parent):
            if node == destination:
                return True
            visited.add(node)
            for nei in graph[node]:
                if nei != parent and nei not in visited:
                    if dfs(nei, node):
                        return True
                        
            return False
        
        graph = defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        visited = set()
        return dfs(source, -1)