class Solution:
    def findLeastNumOfUniqueInts(self, nums: List[int], k: int) -> int:
        if k == len(nums):
            return 0

        d = Counter(nums)
        ans = len(d)
        if k == 0:
            return ans
        
        arr = sorted(d, key = lambda x : d[x])
        for i in arr:
            if d[i] > k:
                d[i] -= k
                k = 0
            else:
                k -= d[i]
                del d[i]

            if k == 0:
                return len(d)