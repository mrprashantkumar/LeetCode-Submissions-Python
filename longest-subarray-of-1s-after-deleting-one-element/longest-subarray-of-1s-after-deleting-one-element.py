class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if 0 not in nums:
            return n-1
        if 1 not in nums:
            return 0
        
        pref = [0]*n
        c = 0
        for i in range(n):
            if nums[i] == 1:
                c += 1
            else:
                c = 0
            pref[i] = c
        
        suff = [0]*n
        c = 0
        for i in range(n-1, -1, -1):
            if nums[i] == 1:
                c += 1
            else:
                c = 0
            suff[i] = c

        ans = max(pref)
        for i in range(1, n-1):
            if nums[i] == 0:
                ans = max(ans, pref[i-1]+suff[i+1])
        return ans