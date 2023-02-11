class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = defaultdict(lambda:set())
        for re in redEdges:
            graph[re[0]].add((re[1],1))
            
        for be in blueEdges:
            graph[be[0]].add((be[1],0))
        
        res = [float('inf') for _ in range(n)]
        res[0] = 0
        queue = [(0,2,0)]
        visited = set()
        
        while queue:
            node_id,node_color,nd = queue.pop(0)
            res[node_id] = min(res[node_id],nd)
            
            for neighbour in graph[node_id]:
                
                nid,nc = neighbour
                
                if (nid,nc) not in visited and (node_color == 2 or (node_color == 1 and nc == 0) or (node_color == 0 and nc == 1)):
                    visited.add((nid,nc))
                    queue.append((nid,nc,nd+1))
                        
        for i,distance in enumerate(res):
            if distance == float('inf'):
                res[i] = -1
        return res