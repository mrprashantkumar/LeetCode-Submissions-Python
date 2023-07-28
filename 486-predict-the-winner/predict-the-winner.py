class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def helper(left, right):
            if left > right:
                return 0
            if dp[left][right] != -1:
                return dp[left][right]

            first = nums[left] - helper(left+1, right)
            last = nums[right] - helper(left, right-1)

            dp[left][right] = max(first, last)
            return dp[left][right]
        
        n = len(nums)
        if n <= 2:
            return True
        
        dp = [[-1]*n for _ in range(n+1)]
        return helper(0, n-1) >= 0