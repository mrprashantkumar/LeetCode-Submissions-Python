#User function Template for python3

import sys
sys.setrecursionlimit(10**8)
class Solution:
    def numIslands(self,grid):
        n, m = len(grid), len(grid[0])
        visited = [[False]*m for _ in range(n)]
        
        def check(p, q):
            return 0<=p<n and 0<=q<m and grid[p][q] == 1 and not visited[p][q]
        
        def dfs(x, y):
            visited[x][y] = True
            for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                if check(x+dx, y+dy):
                    dfs(x+dx, y+dy)
            
        
        ans = 0
        for i in range(n):
            for j in range(m):
                if not visited[i][j]and grid[i][j] == 1:
                    dfs(i, j)
                    ans += 1
        return ans


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
        print(obj.numIslands(grid))
# } Driver Code Ends