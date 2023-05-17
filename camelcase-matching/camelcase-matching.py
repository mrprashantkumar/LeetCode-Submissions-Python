class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def compare(s, t):
            n = len(s)
            i, j = 0, 0
            while i<n and j<m:
                if s[i] == t[j]:
                    i += 1
                    j += 1
                elif s[i].isupper():
                    return False
                else:
                    i += 1
            while i<n:
                if s[i].isupper():
                    return False
                i += 1
            return j == m

        m = len(pattern)
        ans = []
        for word in queries:
            ans.append(compare(word, pattern))
        return ans