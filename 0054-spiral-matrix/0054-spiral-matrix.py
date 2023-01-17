class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n, ans = len(matrix), len(matrix[0]), []
        total = m*n
        rs, cs, re, ce = 0, 0, m-1, n-1

        c=0
        while c<total:
            i = cs
            while c<total and i<=ce:
                ans.append(matrix[rs][i])
                c+=1
                i+=1
            rs+=1

            i = rs
            while c<total and i<=re:
                ans.append(matrix[i][ce])
                c+=1
                i+=1
            ce-=1

            i=ce
            while c<total and i>=cs:
                ans.append(matrix[re][i])
                c+=1
                i-=1
            re-=1

            i=re
            while c<total and i>=rs:
                ans.append(matrix[i][cs])
                c+=1
                i-=1
            cs+=1
        
        return ans