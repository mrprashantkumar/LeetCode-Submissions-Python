class DisjointSet:
    def __init__(self, n):
        self.rank = [0]*(n+1)
        self.parent = [i for i in range(n+1)]
    
    def find(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, u, v):
        paru = self.find(u)
        parv = self.find(v)
        
        if paru == parv:
            return
        
        if self.rank[paru] < self.rank[parv]:
            self.parent[paru] = parv
        elif self.rank[paru] < self.rank[parv]:
            self.parent[parv] = paru
        else:
            self.parent[parv] = paru
            self.rank[paru] += 1

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        obj = DisjointSet(n)
        ans = []
        for u, v in edges:
            if obj.find(u) != obj.find(v):
                obj.union(u, v)
            else:
                return [u, v]