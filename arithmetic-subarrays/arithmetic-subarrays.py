class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def helper(x, y):
            mini, maxi = min(nums[x:y+1]), max(nums[x:y+1])
            if (maxi-mini)%(y-x) != 0:
                return False
            diff = (maxi-mini)//(y-x)
            if not diff:
                return mini == maxi
            seen = set(nums[x:y+1])
            for k in range(mini, maxi, diff):
                if k not in seen:
                    return False
            return True

        n, m = len(nums), len(l)
        ans = []
        for i, j in zip(l, r):
            ans.append(helper(i, j))
        return ans