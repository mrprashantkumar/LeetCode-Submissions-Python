class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        seen = set()
        maxi = nums[0]
        ans = 0
        for i in nums:
            if i not in seen:
                seen.add(i)
                maxi = i
            else:
                ans += (maxi + 1 - i)
                maxi += 1

            seen.add(maxi)
        return ans