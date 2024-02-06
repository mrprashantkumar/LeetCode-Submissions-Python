class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n, k = len(s), len(p)
        if k > n:
            return []

        freqP = [0]*26
        freqS = [0]*26
        for i in range(k-1):
            freqP[ord(p[i])-97] += 1
            freqS[ord(s[i])-97] += 1
        freqP[ord(p[k-1])-97] += 1
        
        
        ans = []
        for i in range(k-1, n):
            freqS[ord(s[i])-97] += 1
            if freqP == freqS:
                ans.append(i-k+1)
            freqS[ord(s[i-k+1])-97] -= 1
        return ans