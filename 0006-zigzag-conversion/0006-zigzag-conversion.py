class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        n = len(s)
        mat = [[0]*n for _ in range(numRows)]
        r, c = 0, 0
        i = 0
        while i<n:
            r = 0
            while r<numRows and i<n:
                mat[r][c] = s[i]
                i += 1
                r += 1
            r = numRows-2
            c += 1
            while i<n and r>0:
                mat[r][c] = s[i]
                r -= 1
                c += 1
                i += 1
        
        ans = ""
        for i in range(numRows):
            for j in range(n):
                if mat[i][j] != 0:
                    ans += mat[i][j]
        return ans
                
                
        