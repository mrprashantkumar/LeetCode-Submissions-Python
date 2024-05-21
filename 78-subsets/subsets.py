class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        
        ele = [nums[0]]
        res = self.subsets(nums[1:])

        ans = [arr[:] for arr in res]
        ans += [arr[:]+ele for arr in res]
        return ans