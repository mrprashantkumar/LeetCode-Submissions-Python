class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        d = Counter(nums)
        if k == 0:
            return sum([d[i] >= 2 for i in d])
        ans = 0
        for i in d:
            if i+k in d:
                ans += 1
        return ans