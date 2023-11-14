class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        d = defaultdict(list)
        for i, x in enumerate(s):
            d[x].append(i)
        
        ans = 0
        for ch in d:
            start, end = d[ch][0], d[ch][-1]
            ans += len(set(s[start+1 : end]))
        return ans