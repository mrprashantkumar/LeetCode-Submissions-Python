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
            
from typing import List
class Solution:
    def numOfIslands(self, rows: int, cols : int, operators : List[List[int]]) -> List[int]:
        def isvalid(p, q):
            return 0<=p<rows and 0<=q<m
            
        obj = DisjointSet(rows*cols)
        visited = set()
        n = len(operators)
        ans = []
        curr = 0
        for x, y in operators:
            num = x*cols + y
            if num not in visited:
                curr += 1
                visited.add(num)
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    if isvalid(x+dx, y+dy):
                        newcord = cols*(x+dx) + y+dy
                        if newcord in visited:
                            if obj.find(num) != obj.find(newcord):
                                curr -= 1
                                obj.union(num, newcord)
            # print(x, y, visited)
            ans.append(curr)
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3


    
if __name__=="__main__":
    T = int(input())
    for t in range(T):
        
        n = int(input())
        m = int(input())
        k = int(input())
        operators = []
        for i in range(k):
            u, v = map(int, input().strip().split())
            operators.append([u, v])
        obj = Solution()
        ans = obj.numOfIslands(n, m, operators)
        for i in ans:
            print(i, end = ' ')
        print()
            

# } Driver Code Ends