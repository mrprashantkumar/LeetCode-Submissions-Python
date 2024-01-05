setrecursionlimit(10**8)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        seen = []
        for i in nums:
            if not seen or seen[-1]<i:
                seen.append(i)
            else:
                ind = bisect_left(seen, i)
                seen[ind] = i
        return len(seen)
        
        
#         # dp = [1] * n
#         # for i in range(n):
#         #     for j in range(i):
#         #         if nums[i]>nums[j]:
#         #             dp[i] = max(dp[i], dp[j]+1)
#         # return max(dp)