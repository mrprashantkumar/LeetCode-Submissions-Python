class Solution:
    def countGoodNumbers(self, n: int) -> int:
        def getpow(n, m):
            if m==0:
                return 1
            
            ans = 1
            smans = getpow(n, m//2)
            if m&1:
                ans *= n
            ans *= smans*smans
            ans %= 1000000007
            return ans
            
        
        return getpow(5, (n+1)//2) * getpow(4, n//2) % 1000000007