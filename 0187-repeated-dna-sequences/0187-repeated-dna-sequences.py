class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        seen = set()
        ans = []
        for i in range(n-10+1):
            sub = s[i:i+10]
            if sub in seen:
                ans.append(sub)
            seen.add(sub)
        return list(set(ans))