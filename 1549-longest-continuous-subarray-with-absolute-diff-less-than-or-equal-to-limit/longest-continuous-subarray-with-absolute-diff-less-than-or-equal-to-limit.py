class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        minqu, maxqu = [], []
        left = 0
        ans = 0
        for right in range(n):
            heappush(minqu, (nums[right], right))
            heappush(maxqu, (-nums[right], right))
            while -maxqu[0][0] - minqu[0][0] > limit:
                left = min(maxqu[0][1], minqu[0][1]) + 1

                while maxqu[0][1] < left:
                    heappop(maxqu)
                while minqu[0][1] < left:
                    heappop(minqu)
            
            ans = max(ans, right - left + 1)
        
        return ans