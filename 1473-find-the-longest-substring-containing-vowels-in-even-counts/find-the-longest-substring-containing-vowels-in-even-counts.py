class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        memo = {0:0}
        tmp = {'a':0,'e':1,'i':2,'o':3,'u':4}
        cur, ans = 0,0
        for i, x in enumerate(s, 1):
            if x in tmp:
                cur ^= 1 << tmp[x]
            if cur in memo:
                ans = max(ans, i - memo[cur])
            else:
                memo[cur] = i
        return ans