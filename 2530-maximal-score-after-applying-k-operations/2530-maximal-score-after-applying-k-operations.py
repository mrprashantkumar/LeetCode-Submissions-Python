class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heapq._heapify_max(nums)
        ans=0
        for _ in range(k):
            ans += nums[0]
            heapq._heapreplace_max(nums, (nums[0]+2)//3)
        return ans