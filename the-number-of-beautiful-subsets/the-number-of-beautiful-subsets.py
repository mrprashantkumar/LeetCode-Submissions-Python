class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        def helper(i, arraysofar):
            if i >= n:
                if arraysofar:
                    return 1
                return 0
            
            ans = 0
            ans += helper(i+1, arraysofar)
            if nums[i]-k not in arraysofar:
                ans += helper(i+1, arraysofar+[nums[i]])
            return ans

        n = len(nums)
        nums.sort()
        return helper(0, [])