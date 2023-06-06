class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        freq = defaultdict(int)
        for i in nums:
            freq[i%space] += 1
        maxi = max(freq.values())
        ans = 1000000007
        for i in nums:
            if freq[i%space] == maxi:
                ans = min(ans, i)
        return ans
