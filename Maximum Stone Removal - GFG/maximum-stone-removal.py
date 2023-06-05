#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
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
    def maxRemove(self, adj, n):
        row, col = 0, 0
        for i, j in adj:
            row = max(row, i)
            col = max(col, j)
        
        obj = DisjointSet(row+col+3)
        d = {}
        for x, y in adj:
            obj.union(x, y+row+1)
            d[x] = 1
            d[y+row+1] = 1
        
        ans = 0
        for i in d:
            if i == obj.find(i):
                ans += 1
        return n-ans




#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n = int(input())
        adj = [list(map(int, input().split())) for _ in range(n)]
        ob = Solution()
        res = ob.maxRemove(adj, n)
        print(res)
# } Driver Code Ends