class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache
        def helper(target):
            if target == 0:
                return 1
            
            ans=0
            for i in nums:
                if i<=target:
                    ans += helper(target-i)

            return ans
        
        nums.sort()
        return helper(target)