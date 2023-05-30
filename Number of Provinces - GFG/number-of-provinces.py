#User function Template for python3
class DisjointSet:
    def __init__(self, n):
        self.rank = [0]*(n+1)
        self.size = [1]*(n+1)
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
    def numProvinces(self, adj, V):
        obj = DisjointSet(V)
        for i in range(V):
            for j in range(V):
                if adj[i][j] == 1:
                    obj.union(i, j)
        ans = 0
        for i in range(V):
            if obj.parent[i] == i:
                ans += 1
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        V=int(input())
        adj=[]
        
        for i in range(V):
            temp = list(map(int,input().split()))
            adj.append(temp);
        
        ob = Solution()
        print(ob.numProvinces(adj,V))
# } Driver Code Ends