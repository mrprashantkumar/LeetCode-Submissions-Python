class Solution:
    def reverseParentheses(self, s: str) -> str:
        def helper(i):
            if i >= n:
                return n, ''
            
            curr = ''
            j = i
            while j < n:
                if s[j] == '(':
                    ind, smans = helper(j+1)
                    curr += smans
                    j = ind
                elif s[j] == ')':
                    curr = curr[::-1]
                    return j+1, curr
                else:
                    curr += s[j]
                    j += 1
            
            return j, curr

        n = len(s)
        return helper(0)[1]