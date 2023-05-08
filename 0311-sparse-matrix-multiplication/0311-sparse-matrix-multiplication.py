class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        x, y, z = len(mat1), len(mat1[0]), len(mat2[0])
        ans = [[0]*z for _ in range(x)]
        
        for i in range(x):
            for j in range(z):
                for k in range(y):
                    ans[i][j] += mat1[i][k] * mat2[k][j]
        
        return ans