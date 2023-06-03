class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        def dfs(node, parent):
            visited.add(node)
            for nei in graph[node]:
                if nei != parent and nei not in visited and nei not in restricted:
                    dfs(nei, node)
            return
        
        graph = defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        visited = set()
        restricted = set(restricted)
        dfs(0, -1)
        return len(visited)