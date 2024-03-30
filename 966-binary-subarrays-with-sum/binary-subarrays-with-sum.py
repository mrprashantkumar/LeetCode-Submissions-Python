class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        d = Counter()
        d[0] = 1
        ans = 0
        pref = 0
        for i in nums:
            pref += i
            if pref - goal in d:
                ans += d[pref - goal]
            
            d[pref] += 1
            
        return ans