class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0]*n for _ in range(n)]
        
        num = 1
        rs, cs, re, ce = 0, 0, n-1, n-1
        total = n*n
        
        while num <= total:
            i=cs
            while num<=total and i<=ce:
                ans[rs][i] = num
                num+=1
                i+=1
            rs+=1
            
            i=rs
            while num<=total and i<=re:
                ans[i][ce] = num
                num+=1
                i+=1
            ce-=1
            
            i=ce
            while num<=total and i>=cs:
                ans[re][i] = num
                num+=1
                i-=1
            re-=1
            
            i=re
            while num<=total and i>=rs:
                ans[i][cs] = num
                num+=1
                i-=1
            cs+=1
        
        return ans