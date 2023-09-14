class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        n = len(nums)
        d = defaultdict(int)
        ans = 0
        left = 0
        pref = 0

        for i in range(k-1):
            d[nums[i]] += 1
            pref += nums[i]
        
        for i in range(n-k+1):
            d[nums[i+k-1]] += 1
            pref += nums[i+k-1]

            if len(d) >= m:
                ans = max(ans, pref)
            
            pref -= nums[i]
            d[nums[i]] -= 1
            if d[nums[i]] == 0:
                del d[nums[i]]
        
        return ans