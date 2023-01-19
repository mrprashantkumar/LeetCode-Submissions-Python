class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans = 0
        mod = [0]*k
        mod[0]=1
        
        pref = list(accumulate(nums))
        for i in pref:
            ans += mod[i%k]
            mod[i%k] += 1
        return ans