class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        op, cl = 0, 0

        for i in s:
            if i == '(':
                op += 1
            else:
                if op > 0:
                    op -= 1
                else:
                    cl += 1
        
        return op + cl