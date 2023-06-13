class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        colgrid  =[]
        for j in range(n):
            col = []
            for i in range(n):
                col.append(grid[i][j])
            colgrid.append(col)
        
        ans=0
        for row in grid:
            for col in colgrid:
                if row == col:
                    ans+=1
        return ans