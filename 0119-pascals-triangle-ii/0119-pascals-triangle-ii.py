class Solution:
    def getRow(self, n: int) -> List[int]:
        ans = [[1]*i for i in range(1, n+2)]
        
        for i in range(2, n+1):
            for j in range(1, i):
                ans[i][j] = ans[i-1][j]+ans[i-1][j-1]
        return ans[-1]