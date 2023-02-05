class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p = sorted(p)
        k = len(p)
        n = len(s)
        ans = []
        
        for i in range(n-k+1):
            sub = s[i:i+k]
            if sorted(sub)==p:
                ans.append(i)
        return ans