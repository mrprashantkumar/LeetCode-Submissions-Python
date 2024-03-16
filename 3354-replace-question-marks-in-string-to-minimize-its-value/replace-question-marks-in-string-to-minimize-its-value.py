class Solution:
    def minimizeStringValue(self, s: str) -> str:
        res = []
        d = {chr(i+97):0 for i in range(26)}
        for i in s:
            if i != '?':
                d[i] += 1
        for i in s:
            if i == '?':
                ch = sorted(d.keys(), key = lambda x : d[x])[0]
                res.append(ch)
                d[ch] += 1
                
        res.sort(reverse = True)
        ans = ''
        for i in s:
            if i == '?':
                ans += res.pop()
            else:
                ans += i
        return ans