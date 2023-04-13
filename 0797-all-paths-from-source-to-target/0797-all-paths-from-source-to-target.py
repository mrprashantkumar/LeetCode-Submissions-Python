class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        ans = []
        
        qu = deque()
        qu.append((0, [0]))
        while qu:
            node, pathsofar = qu.popleft()
            if node == n-1:
                ans.append(pathsofar)
            
            for nei in graph[node]:
                qu.append((nei, pathsofar+[nei]))
            
        return ans