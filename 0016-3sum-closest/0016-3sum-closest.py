class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans=0
        diff=99999999
        n = len(nums)
        nums.sort()
        for i in range(n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            
            newT = target-nums[i]
            
            lo, hi = i+1, n-1
            while lo<hi:
                pair = nums[lo]+nums[hi]
                if pair==newT:
                    return target
                elif pair>newT:
                    if pair-newT<diff:
                        diff = pair-newT
                        ans = nums[i]+nums[lo]+nums[hi]
                    hi-=1
                else:
                    if newT-pair<diff:
                        diff = newT-pair
                        ans = nums[i]+nums[lo]+nums[hi]
                    lo+=1
        return ans