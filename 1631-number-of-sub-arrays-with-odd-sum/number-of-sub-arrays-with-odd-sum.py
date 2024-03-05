class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        d = defaultdict(int)
        d[0] = 1
        ans = 0
        pref = 0
        for i in range(n):
            pref += arr[i]
            pref %= 2
            d[pref] += 1
            ans += d[1 - pref]
            ans %= 1000000007
        return ans