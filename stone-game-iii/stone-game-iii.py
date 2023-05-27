class Solution:
    def stoneGameIII(self, nums: List[int]) -> str:
        def helper(i):
            if i >= n:
                return 0
                
            if dp[i] != -1:
                return dp[i]

            ans = nums[i] - helper(i+1)
            if i+1 < n:
                ans = max(ans, nums[i]+nums[i+1]-helper(i+2))
            if i+2 < n:
                ans = max(ans, nums[i]+nums[i+1]+nums[i+2] - helper(i+3))
            
            dp[i] = ans
            return ans
        
        n = len(nums)
        dp = [-1]*(n+1)
        res = helper(0)
        if res > 0:
            return "Alice"
        elif res < 0:
            return "Bob"
        return "Tie"