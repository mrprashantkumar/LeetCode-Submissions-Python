class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        def helper(i):
            res = 1
            start = nums[i]
            for j in range(i+1, n):
                if (j-i)&1:
                    if nums[j] == nums[j-1]+1:
                        res += 1
                    else:
                        break
                else:
                    if nums[j] == start:
                        res += 1
                    else:
                        break
            return res
        
        n = len(nums)
        ans = 0
        for a in range(n):
            ans = max(ans, helper(a))
        if ans > 1:
            return ans
        return -1