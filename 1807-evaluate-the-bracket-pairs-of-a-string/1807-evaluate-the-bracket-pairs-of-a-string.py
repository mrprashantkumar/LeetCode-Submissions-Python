class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        d = {}
        for key, value in knowledge:
            d[key] = value
        n = len(s)
        ans = ''
        i = 0
        while i<n:
            if s[i] == '(':
                i += 1
                c = ""
                while i<n and s[i] != ')':
                    c += s[i]
                    i += 1
                    
                if c in d:
                    ans += d[c]
                else:
                    ans += "?"
            else:
                ans += s[i]
            i += 1
        return ans