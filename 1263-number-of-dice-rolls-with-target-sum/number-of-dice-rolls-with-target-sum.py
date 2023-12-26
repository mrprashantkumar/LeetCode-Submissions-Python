class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        @cache
        def helper(i, target):
            if i == n:
                return int(target == 0)
            
            if target < 0:
                return 0
            
            ans = 0
            for j in range(1, k+1):
                ans += helper(i+1, target - j)
            return ans % 1000000007
        
        return helper(0, target)