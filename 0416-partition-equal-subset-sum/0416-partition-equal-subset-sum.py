class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total, n = 0, 0
        for i in nums:
            total += i
            n += 1
            
        if total&1:
            return False
        
        def helper(i, target):
            if i==n-1:
                if target==nums[i]:
                    return True
                return False
            
            if target < 0:
                return False
            elif target == 0:
                return True
            
            if dp[i][target] != -1:
                return dp[i][target]
            
            notTake = helper(i+1, target)
            take = helper(i+1, target-nums[i])
            
            dp[i][target] = take or notTake
            return dp[i][target]
        
        target = total//2
        dp = [[-1]*(target+1) for _ in range(n)]
        return helper(0, target)