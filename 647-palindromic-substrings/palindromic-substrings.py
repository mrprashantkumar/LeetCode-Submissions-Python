class Solution:
    def countSubstrings(self, s: str) -> int:
        @cache
        def pal(l,r):
            count = 0
            while l >= 0 and r < n and s[l] == s[r]:
                count +=1
                l -=1
                r +=1
            return count
        
        ans = 0
        n = len(s)
        for i in range(n):
            ans += pal(i,i) #for odd len
            ans += pal(i,i+1) #for even len
        return ans