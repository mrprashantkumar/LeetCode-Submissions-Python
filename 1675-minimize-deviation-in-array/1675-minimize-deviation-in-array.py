class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        n = len(nums)
        
        ans = 1000000007
        mini = 1000000007
        for i in range(n):
            if nums[i]&1:
                nums[i]*=2
            mini = min(mini, nums[i])
        
        heapq._heapify_max(nums)
        
        while nums[0]%2 == 0:
            ans = min(ans, nums[0]-mini)
            mini = min(mini, nums[0]//2)
            heapq._heapreplace_max(nums, nums[0]//2)
        
        return min(ans, nums[0]-mini)