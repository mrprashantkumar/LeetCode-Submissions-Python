class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        def simulate(col):
            i=0
            while 0<=col<n and i<m:
                # print(i, col)
                if grid[i][col]==1:
                    if col<n-1 and grid[i][col+1]==1:
                        i += 1
                        col += 1
                    else:
                        return -1
                else:
                    if col>0 and grid[i][col-1]==-1:
                        i += 1
                        col -= 1
                    else:
                        return -1
            return col
                
        
        
        m, n = len(grid), len(grid[0])
        ans = []
        for i in range(n):
            ans.append(simulate(i))
        return ans