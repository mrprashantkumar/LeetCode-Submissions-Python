class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])

        row, col = defaultdict(int), defaultdict(int)

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    row[i] += 1
                    col[j] += 1
        
        ans = 0
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    if row[i] == col[j] == 1:
                        ans += 1
        return ans