class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def helper(k, s, lenS):
            if k == 0:
                return ''.join(s)
            
            fact = factorial(lenS-1)
            ind = k//fact
            k %= fact
            return s[ind] + helper(k, s[:ind]+s[ind+1:], lenS-1)
        
        s = [str(i) for i in range(1, n+1)]
        return helper(k-1, s, n)