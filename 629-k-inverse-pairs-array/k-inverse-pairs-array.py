class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        @cache
        def helper(n, k):
            if k == 0:
                return 1
            
            if n <= 0 or k < 0:
                return 0
            
            ans = helper(n, k-1) + helper(n-1, k) - helper(n-1, k-n)
            return ans % 1000000007
        
        return helper(n, k)