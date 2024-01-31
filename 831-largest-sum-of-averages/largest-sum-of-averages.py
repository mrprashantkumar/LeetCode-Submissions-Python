class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        @cache
        def helper(i, k):
            if k == 1:
                return sum(nums[i:])/(n-i)
            
            ans, pref, c = 0, 0, 0
            for j in range(i, n-1):
                c += 1
                pref += nums[j]
                ans = max(ans, pref/c + helper(j+1, k-1))
            return ans
        
        n = len(nums)
        return helper(0, k)