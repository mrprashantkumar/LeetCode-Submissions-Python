from typing import List
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
    
    def unionSize(self, u, v):
        paru = self.find(u)
        parv = self.find(v)
        
        if paru == parv:
            return
        
        if self.size[paru] < self.size[parv]:
            self.parent[paru] = parv
            self.size[parv] += self.size[paru]
        else:
            self.parent[parv] = paru
            self.size[paru] += self.size[parv]

class Solution:
    def MaxConnection(self, grid : List[List[int]]) -> int:
        def isvalid(p, q):
            return 0<=p<n and 0<=q<m and grid[p][q] == 1
            
        n, m = len(grid), len(grid[0])
        obj = DisjointSet(n*m)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    cellVal = i*m + j
                    for di, dj in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                        if isvalid(i+di, j+dj):
                            newCell = (i+di)*m + j+dj
                            if obj.find(cellVal) != obj.find(newCell):
                                obj.unionSize(cellVal, newCell)
        
        ans = max(obj.size)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    cellVal = i*m + j
                    currset = set()
                    for di, dj in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                        if isvalid(i+di, j+dj):
                            newCell = (i+di)*m + j+dj
                            currset.add(obj.find(newCell))
                    curr = 1
                    for x in currset:
                        curr += obj.size[x]
                    ans = max(ans, curr)
        return ans


#{ 
 # Driver Code Starts
class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        grid=IntMatrix().Input(n, n)
        
        obj = Solution()
        res = obj.MaxConnection(grid)
        
        print(res)
        

# } Driver Code Ends