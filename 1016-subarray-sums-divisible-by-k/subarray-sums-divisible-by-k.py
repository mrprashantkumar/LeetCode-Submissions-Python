class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pref = 0
        d = {0:1}
        ans = 0
        for i in nums:
            pref += i
            pref %= k
            ans += d.get(pref, 0)
            d[pref] = d.get(pref, 0) + 1
        
        return ans