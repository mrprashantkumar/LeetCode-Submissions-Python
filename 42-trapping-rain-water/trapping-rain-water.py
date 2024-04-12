class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        
        suffMax = [0]*n
        suffMax[-1] = height[-1]
        for i in range(n-2, -1, -1):
            suffMax[i] = max(height[i], suffMax[i+1])
        
        ans=0
        maxsoFar = height[0]
        for i in range(n):
            maxsoFar = max(maxsoFar, height[i])
            ans += min(maxsoFar, suffMax[i])-height[i]
        return ans