class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1]*(n+1)
        l1, l2, l3 = 1, 1, 1
        
        for i in range(2, n+1):
            n1 = dp[l1]*2
            n2 = dp[l2]*3
            n3 = dp[l3]*5
            mini = min(n1, n2, n3)
            dp[i] = mini
            if n1 == mini:
                l1 +=1
            if n2 == mini:
                l2 +=1
            if n3 == mini:
                l3 +=1
        
        return dp[n]