class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        d = Counter(nums)
        ans = []
        for i in d:
            if d[i] == 1:
                ans.append(i)
        return ans