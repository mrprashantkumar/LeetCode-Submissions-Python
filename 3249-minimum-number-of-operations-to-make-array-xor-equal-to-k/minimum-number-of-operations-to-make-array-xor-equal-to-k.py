class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        x = 0
        for i in nums:
            x ^= i
        
        if x == k:
            return 0
        
        val = x^k
        ans = 0
        while val:
            ans += val&1
            val //= 2
        return ans