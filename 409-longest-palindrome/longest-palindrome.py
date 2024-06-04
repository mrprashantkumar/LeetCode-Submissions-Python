class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = Counter(s)
        flag = False
        ans=0
        for i in d:
            if d[i]%2==0:
                ans += d[i]
            else:
                ans += (d[i]-1)
                flag = True
        if flag:
            ans += 1
        return ans