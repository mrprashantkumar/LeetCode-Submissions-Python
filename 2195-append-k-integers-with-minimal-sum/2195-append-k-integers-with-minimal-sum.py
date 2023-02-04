class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        seen = set(nums)
        n = len(nums)
        ans = k*(k+1)//2
        k  += 1
        for i in sorted(seen):
            if i<k:
                ans -= i
                ans += k
                k += 1
        return ans