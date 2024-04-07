class Solution:
    def checkValidString(self, s: str) -> bool:
        @cache
        def helper(i, open):
            if open < 0:
                return False
            if i == n:
                return open == 0
            
            if s[i] == '(':
                return helper(i+1, open+1)
            elif s[i] == ')':
                return helper(i+1, open-1)
            else:
                return helper(i+1, open) or helper(i+1, open+1) or helper(i+1, open-1)
        
        n = len(s)
        return helper(0, 0)