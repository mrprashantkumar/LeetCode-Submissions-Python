class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        ans = 0
        
        for i in range(n):
            ans += mat[i][i]
            ans += mat[i][n-i-1]
        
        if n&1:
            ans -= mat[n//2][n//2]
        
        return ans