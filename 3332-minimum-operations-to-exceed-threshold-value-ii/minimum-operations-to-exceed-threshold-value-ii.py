class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        heapify(nums)
        ans = 0
        while n >= 2:
            a = heappop(nums)
            b = heappop(nums)
            if a >= k:
                break
            heappush(nums, min(a, b)*2 + max(a, b))
            ans += 1
            n -= 1
        return ans