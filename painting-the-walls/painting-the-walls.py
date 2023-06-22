class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        def helper(i, wallLeft):
            if wallLeft <= 0:
                return 0
            if i >= n:
                return 1000000007
            
            if dp[i][wallLeft] != -1:
                return dp[i][wallLeft]
            
            notTake = helper(i+1, wallLeft)
            take = cost[i] + helper(i+1, wallLeft - time[i] - 1)

            dp[i][wallLeft] = min(take, notTake)
            return dp[i][wallLeft]

        n = len(cost)
        dp = [[-1]*(n+1) for _ in range(n+1)]
        return helper(0, n)