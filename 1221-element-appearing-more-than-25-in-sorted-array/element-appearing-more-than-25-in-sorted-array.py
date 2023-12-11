class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        d = Counter(arr)
        ans, maxval = -1, 0
        for i in d:
            if maxval < d[i]:
                ans = i
                maxval = d[i]
        return ans