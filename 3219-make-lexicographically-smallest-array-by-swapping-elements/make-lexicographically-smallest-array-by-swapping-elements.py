class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        pairs = [(x, i) for i, x in enumerate(nums)]
        pairs.sort()

        ind = []
        for i in range(n):
            if i == 0 or pairs[i][0] - pairs[i-1][0] > limit:
                ind.append([])
            ind[-1].append(pairs[i][1])
        
        ans = [0]*n
        for arr in ind:
            sarr = sorted(arr)
            for j in range(len(arr)):
                ans[sarr[j]] = nums[arr[j]]
        return ans