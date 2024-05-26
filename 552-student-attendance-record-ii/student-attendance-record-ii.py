class Solution:
    def checkRecord(self, n: int) -> int:
        def helper(i, can_absent, can_late):
            if i > n:
                return 0
            if i == n:
                return 1
            
            if (i, can_absent, can_late) in dp:
                return dp[(i, can_absent, can_late)]
            
            res = helper(i+1, can_absent, True)

            if can_absent:
                res += helper(i+1, not can_absent, True)

            if can_late:
                res += helper(i+1, can_absent, not can_late)
                res += helper(i+2, can_absent, not can_late)
            
            res %= 1000000007
            dp[(i, can_absent, can_late)] = res
            return res
        
        #tabulation
        dp = [[[0]*(2) for i in range(2)] for j in range(n+2)]

        for j in range(2):
            for k in range(2):
                dp[n][j][k] = 1
                
        for i in range(n-1, -1, -1):
            for can_absent in range(1, -1, -1):
                for can_late in range(1, -1, -1):

                    res = dp[i+1][can_absent][1]
                    if can_absent:
                        res += dp[i+1][1 - can_absent][1]

                    if can_late:
                        res += dp[i+1][can_absent][1 - can_late]
                        res += dp[i+2][can_absent][1 - can_late]
                    
                    res %= 1000000007
                    dp[i][can_absent][can_late] = res
        
        return dp[0][1][1]