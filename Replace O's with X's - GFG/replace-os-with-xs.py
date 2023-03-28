#User function Template for python3
from collections import *
class Solution:
    def fill(self, n, m, grid):
        visited = set()
        qu = deque()
        for j in range(m):
            if grid[0][j] == 'O':
                qu.append((0, j))
                visited.add((0, j))
            if grid[n-1][j] == 'O':
                qu.append((n-1, j))
                visited.add((n-1, j))
        for i in range(n):
            if grid[i][0] == 'O':
                qu.append((i, 0))
                visited.add((i, 0))
            if grid[i][m-1] == 'O':
                qu.append((i, m-1))
                visited.add((i, m-1))
        # print(visited)
        def isvalid(p, q):
            return 0<=p<n and 0<=q<m and grid[p][q] == 'O' and (p, q) not in visited
            
        while qu:
            x, y = qu.popleft()
            for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                if isvalid(x+dx, y+dy):
                    visited.add((x+dx, y+dy))
                    qu.append((x+dx, y+dy))
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 'O':
                    if (i, j) not in visited:
                        grid[i][j] = 'X'
        
        return grid


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        mat = []
        for i in range(n):
            s = list(map(str,input().split()))
            mat.append(s)
        
        ob = Solution()
        ans = ob.fill(n, m, mat)
        for i in range(n):
            for j in range(m):
                print(ans[i][j], end = " ")
            print()
# } Driver Code Ends