class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = [-1]*n
        windowSum = sum(nums[:2*k])
        windowSize = 2*k + 1

        for i in range(k, n-k):
            windowSum += nums[i+k]
            ans[i] = windowSum//windowSize
            windowSum -= nums[i-k]
        
        return ans