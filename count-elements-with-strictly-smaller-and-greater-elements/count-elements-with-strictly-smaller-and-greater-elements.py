class Solution:
    def countElements(self, nums: List[int]) -> int:
        d, mini, maxi = {}, 10000007, -10000007
        for i in nums:
            d[i] = d.get(i, 0) + 1
            mini = min(mini, i)
            maxi = max(maxi, i)
        del d[mini]
        if mini != maxi:
            del d[maxi]
        
        return sum(d.values())