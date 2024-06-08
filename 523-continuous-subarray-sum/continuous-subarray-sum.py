class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d = defaultdict(int)
        d[0] = -1
        pref = 0
        for i, x in enumerate(nums):
            pref += x
            pref %= k
            print(i, pref)
            d[pref] = min(d.get(pref, inf), i)
            if pref in d and (i - d[pref]) >= 2:
                return True
            
        return False