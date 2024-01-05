setrecursionlimit(10**8)
class Solution:
    def lengthOfLIS(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[0]*(n+1) for _ in range(n+1)]
        for i in range(n-1, -1, -1):
            for prev in range(i-1, -2, -1):
                notTake = dp[i+1][prev+1]
                take = 0
                if prev == -1 or arr[i]>arr[prev]:
                    take = 1+dp[i+1][i+1]

                dp[i][prev+1] = max(take, notTake)
        
        return dp[0][0]