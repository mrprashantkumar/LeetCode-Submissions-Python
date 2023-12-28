class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @cache
        def helper(i, curr, lensofar, k):
            if i == n:
                return 0
            
            notTake = inf
            if k > 0:
                notTake = helper(i+1, curr, lensofar, k-1)
            
            take = 0
            if s[i] == curr:
                val = 0
                if lensofar == 1 or len(str(lensofar + 1)) > len(str(lensofar)):
                    val = 1
                take = val + helper(i+1, curr, lensofar+1, k)
            else:
                take = 1 + helper(i + 1, s[i], 1, k)
            
            return min(take, notTake)
        
        n = len(s)
        return helper(0, '', 0, k)