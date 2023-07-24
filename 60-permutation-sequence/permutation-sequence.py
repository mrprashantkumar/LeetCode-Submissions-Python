class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        s = [str(i) for i in range(1, n+1)]
        ans = ''
        fact = factorial(n)
        k -= 1
        while k != 0:
            fact //= n
            ind = k//fact
            k %= fact
            ans += s[ind]
            s = s[:ind]+s[ind+1:]
            n -= 1
        
        ans += ''.join(s)
        return ans