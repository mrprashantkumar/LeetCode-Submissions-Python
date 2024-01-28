class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        n, m = len(matrix), len(matrix[0])
        for row in matrix:
            for j in range(m-1):
                row[j+1] += row[j]
        
        ans = 0
        for j in range(m):
            for i in range(j, m):
                d = defaultdict(int)
                d[0] = 1
                pref = 0
                for k in range(n):
                    pref += matrix[k][i] - (matrix[k][j-1] if j else 0)
                    ans += d[pref - target]
                    d[pref] += 1
        return ans