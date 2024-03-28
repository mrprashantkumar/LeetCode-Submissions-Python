class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        n = len(s)
        ans = ''
        lenans = 0

        for i in range(n):
            curr = set()
            for j in range(i, n):
                curr.add(s[j])
                f = True
                for ch in curr:
                    if ch.lower() not in curr or ch.upper() not in curr:
                        f = False
                        break
                if f and lenans < (j-i+1):
                    lenans = j-i+1
                    ans = s[i:j+1]
        
        return ans