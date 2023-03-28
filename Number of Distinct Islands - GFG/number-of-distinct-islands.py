#User function Template for python3
from collections import *
import sys
sys.setrecursionlimit(10**6)
from typing import List
sys.setrecursionlimit(10**8)
class Solution:
    def countDistinctIslands(self, grid : List[List[int]]) -> int:
        def isvalid(p, q):
            return 0<=p<n and 0<=q<m and grid[p][q] == 1 and (p, q) not in visited
        
        def dfs(x, y, pairs, baserow, basecol):
            visited.add((x, y))
            pairs.append((x-baserow, y-basecol))
            
            for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                if isvalid(x+dx, y+dy):
                    dfs(x+dx, y+dy, pairs, baserow, basecol)
            
        
        n, m = len(grid), len(grid[0])
        visited = set()
        ans = defaultdict(list)
        for i in range(n):
            for j in range(m):
                if isvalid(i, j):
                    pairs = []
                    dfs(i, j, pairs, i, j)
                    ans[tuple(pairs)] = 1
        
        return len(ans)
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().strip().split())
        grid=[]
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        obj=Solution()
        print(obj.countDistinctIslands(grid))
# } Driver Code Ends