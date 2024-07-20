class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        n, m = len(rowSum), len(colSum)
        currRow, currCol = [0]*n, [0]*m
        
        ans = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                ans[i][j] = min(rowSum[i] - currRow[i], colSum[j] - currCol[j])
                currRow[i] += ans[i][j]
                currCol[j] += ans[i][j]
        
        return ans