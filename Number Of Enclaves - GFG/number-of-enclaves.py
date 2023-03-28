#User function Template for python3
from typing import List
import sys
sys.setrecursionlimit(10**7)
class Solution:    
    def numberOfEnclaves(self, grid: List[List[int]]) -> int:
        # code here
        def isvalid(p, q):
            return 0<=p<n and 0<=q<m and grid[p][q] == 1 and (p, q) not in visited
        
        def dfs(x, y):
            visited.add((x, y))
            for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                if isvalid(x+dx, y+dy):
                    dfs(x+dx, y+dy)
        
        n, m = len(grid), len(grid[0])
        visited = set()
        for i in range(n):
            if grid[i][0] == 1 and (i, 0) not in visited:
                dfs(i, 0)
            if grid[i][m-1] == 1 and (i, m-1) not in visited:
                dfs(i, m-1)
        for j in range(m):
            if grid[0][j] == 1 and (0, j) not in visited:
                dfs(0, j)
            if grid[n-1][j] == 1 and (n-1, j) not in visited:
                dfs(n-1, j)
        
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and (i, j) not in visited:
                    ans += 1
        return ans
#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int,input().strip().split())
        grid = []
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])

        obj=Solution()
        print(obj.numberOfEnclaves(grid))
# } Driver Code Ends