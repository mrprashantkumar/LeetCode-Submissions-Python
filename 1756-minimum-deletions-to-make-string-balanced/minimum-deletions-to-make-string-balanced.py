class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        prefB, suffA = [0]*(n), [0]*(n)

        curr = 0
        for i in range(n):
            if s[i] == 'b':
                curr += 1
            prefB[i] = curr
        
        curr = 0
        for i in range(n-1, -1, -1):
            if s[i] == 'a':
                curr += 1
            suffA[i] = curr
        
        prefB, suffA = [0] + prefB + [0], [0] + suffA + [0]
        ans = n
        for i in range(1, n+2):
            ans = min(ans, prefB[i-1] + suffA[i])
        return ans
