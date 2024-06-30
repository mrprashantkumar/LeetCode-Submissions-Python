class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n+1)]
        self.size = [1] * (n+1)
        self.components = n

    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return 0
        if self.size[x] > self.size[y]:
            self.size[x] += self.size[y]
            self.parent[y] = x
        else:
            self.size[y] += self.size[x]
            self.parent[x] = y
        self.components -= 1
        return 1

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice = UnionFind(n)
        bob = UnionFind(n)
        remove = 0
        for t, u, v in edges:
            if t == 3:
                remove += alice.union(u, v) 
                bob.union(u, v)
        
        for t, u, v in edges:
            if t == 1:
                remove += alice.union(u, v)
            else:
                remove += bob.union(u, v)
                
        if alice.components == bob.components == 1:
            return len(edges) - remove
        return -1