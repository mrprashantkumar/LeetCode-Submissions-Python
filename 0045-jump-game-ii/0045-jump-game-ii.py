class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        ans=0
        reach=0
        left, right = 0, 0
        while right < n-1:
            for i in range(left, right+1):
                reach = max(reach, i+nums[i])
            
            left = right+1
            right = reach
            ans+=1
        return ans
        
        
        
        
#         dp = [10000005]*n
#         dp[n-1] = 0
        
#         for i in range(n-2, -1, -1):
#             reach = min(i+nums[i], n-1)
#             for j in range(i+1, reach+1):
#                 dp[i] = min(dp[i], dp[j]+1)
        
#         return dp[0]