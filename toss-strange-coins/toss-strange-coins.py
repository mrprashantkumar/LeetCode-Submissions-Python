class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        def helper(i, target):
            if target < 0:
                return 0

            if i == n:
                return target == 0
            
            if dp[i][target] != -1:
                return dp[i][target]

            notTake = (1 - prob[i]) * helper(i+1, target)
            take = prob[i] * helper(i+1, target - 1)

            dp[i][target] = take + notTake
            return dp[i][target]
        
        n = len(prob)
        dp = [[-1]*(target+1) for _ in range(n)]
        return helper(0, target)