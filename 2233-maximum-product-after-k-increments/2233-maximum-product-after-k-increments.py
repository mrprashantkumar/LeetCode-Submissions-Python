class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        for _ in range(k):
            ele = heapq.heappop(nums)
            ele += 1
            heapq.heappush(nums, ele)
        
        ans = 1
        for i in nums:
            ans *= i
            ans %= 1000000007
        return ans