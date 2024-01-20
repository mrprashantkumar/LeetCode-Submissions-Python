
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        seen = []
        dp = [0] * n
        
        for i in range(n):
            while seen and arr[seen[-1]] >= arr[i]:
                seen.pop()

            if seen:
                smin = seen[-1]
                dp[i] = dp[smin] + (i - smin) * arr[i]
            else:
                dp[i] = (i + 1) * arr[i]
            
            seen.append(i)
            
        return sum(dp) % 1000000007