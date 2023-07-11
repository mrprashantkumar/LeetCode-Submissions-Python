class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        def helper(i, arraySoFar, sumsofar):
            if sumsofar == target:
                res.append(arraySoFar)
                return 

            if i >= n or sumsofar > target:
                return
            
            j = i
            while j<n:
                num = nums[j]
                helper(j+1, arraySoFar+[nums[j]], sumsofar+nums[j])
                while j<n and nums[j] == num:
                    j += 1
                
            return
        
        n = len(nums)
        nums.sort()
        res = []
        helper(0, [], 0)
        return res