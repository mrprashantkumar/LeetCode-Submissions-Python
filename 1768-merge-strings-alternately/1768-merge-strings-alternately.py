class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ''
        i, j = 0, 0
        n, m = len(word1), len(word2)
        while i<n and j<m:
            ans += word1[i]
            ans += word2[j]
            i += 1
            j += 1
        
        while i<n:
            ans += word1[i]
            i += 1
        
        while j<m:
            ans += word2[j]
            j += 1
        
        return ans