class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        def helper(i):
            if i >= n:
                return 0
            
            if dp[i] != -1:
                return dp[i]
            notTake = helper(i+1)
            take = questions[i][0] + helper(i+questions[i][1]+1)
            
            dp[i] = max(take, notTake)
            return dp[i]
        
        n = len(questions)
        dp = [-1]*n
        return helper(0)