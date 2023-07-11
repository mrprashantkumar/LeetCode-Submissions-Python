class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def helper(i, arraySoFar, sumsofar):
            if sumsofar == target:
                res.append(arraySoFar)
                return 

            if i >= n or sumsofar > target:
                return
            
            helper(i+1, arraySoFar, sumsofar)
            helper(i, arraySoFar+[nums[i]], sumsofar+nums[i])
                
            return
        
        n = len(nums)
        nums.sort()
        res = []
        helper(0, [], 0)
        return res