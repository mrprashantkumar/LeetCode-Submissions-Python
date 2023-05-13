class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        def helper(i, last):
            if i == n:
                return 0
            
            if dp[i][last+1] != -1:
                return dp[i][last+1]
            
            notTake = helper(i+1, last)
            take = 0
            if last == -1 or pairs[last][1] < pairs[i][0]:
                take = 1 + helper(i+1, i)
            
            dp[i][last+1] = max(take, notTake)
            return dp[i][last+1]
        
        n = len(pairs)
        pairs.sort()
        dp = [[-1]*(n+1) for _ in range(n+1)]
        return helper(0, -1)