class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
            
        def dfs(node, parent):
            if node in visited:
                return False
            
            visited.add(node)
            for nei in graph[node]:
                if nei != parent:
                    if not dfs(nei, node):
                        return False
            return True
        
        visited = set()
        return dfs(0, -1) and len(visited) == n