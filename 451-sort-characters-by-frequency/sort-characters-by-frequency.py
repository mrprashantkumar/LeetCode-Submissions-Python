class Solution:
    def frequencySort(self, s: str) -> str:
        d = Counter(s)
        return "".join(i*d[i] for i in sorted(d, key = lambda x: d[x], reverse=True))