class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)//2
        d = Counter(nums)
        for key in d:
            if d[key] == n:
                return key