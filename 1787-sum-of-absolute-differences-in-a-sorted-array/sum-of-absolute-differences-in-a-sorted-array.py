class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        t = sum(nums)
        pref = 0

        ans = []
        for i, x in enumerate(nums):
            val = (t - pref - (n-i)*x) + (i*x - pref)
            ans.append(val)
            pref += x
        return ans