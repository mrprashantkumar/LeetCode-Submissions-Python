class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        for i in s:
            d[i] = d.get(i, 0) + 1
        
        arr = sorted(d, key = lambda x: d[x], reverse=True)
        ans = ""
        for i in arr:
            ans += i*d[i]
        return ans