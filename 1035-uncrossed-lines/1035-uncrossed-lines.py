class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        def helper(i, j):
            if i==n or j==m:
                return 0
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            if nums1[i] == nums2[j]:
                dp[i][j] = 1 + helper(i+1, j+1)
                return dp[i][j]
            else:
                dp[i][j] = max(helper(i+1, j), helper(i, j+1))
                return dp[i][j]
        
        n, m = len(nums1), len(nums2)
        dp = [[-1]*m for _ in range(n)]
        return helper(0, 0)