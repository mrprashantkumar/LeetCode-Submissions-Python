class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        def helper(i, j, k):
            if i == n:
                return 0
            
            if j == m:
                return inf
            
            if dp[i][j][k] != -1:
                return dp[i][j][k]
            
            notTake = helper(i, j+1, 0)
            take = inf
            if factory[j][1] > k:
                take = helper(i+1, j, k+1) + abs(robot[i] - factory[j][0])
            
            dp[i][j][k] = min(take, notTake)
            return dp[i][j][k]
        
        n, m = len(robot), len(factory)
        robot.sort()
        factory.sort()
        dp = [[[-1]*100 for a in range(m)] for b in range(n)]
        return helper(0, 0, 0)