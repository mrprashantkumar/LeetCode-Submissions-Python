class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp, count = [1]*n, [1]*n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j]+1
                        count[i] = 0
                    if dp[j] + 1 == dp[i]:
                        count[i] += count[j]
        
        lenans = max(dp)
        ans = 0
        for i in range(n):
            if dp[i] == lenans:
                ans += count[i]
        
        return ans