class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        i, j = 0, n-1
        ans = 0
        while i <= j:
            if nums[i]+nums[j] <= target:
                ans += 2**(j-i)
                ans %= 1000000007
                i += 1
            else:
                j -= 1
        return ans