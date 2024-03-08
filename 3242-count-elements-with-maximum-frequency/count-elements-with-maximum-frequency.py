class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d = Counter(nums)
        maxi = max(d.values())
        ans = 0
        for i, x in d.items():
            if x == maxi:
                ans += x
        return ans