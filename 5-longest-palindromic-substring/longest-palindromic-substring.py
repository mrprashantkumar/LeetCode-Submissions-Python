class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        ans=''
        
        for i in range(l):
            #for odd
            cur=s[i]
            low, high = i-1, i+1
            while low>=0 and high<l and s[low]==s[high]:
                cur = s[low]+cur+s[high]
                low-=1
                high+=1
            if len(cur)>len(ans):
                ans = cur
            
            #for even
            cur=""
            low, high = i, i+1
            while low>=0 and high<l and s[low]==s[high]:
                cur = s[low]+cur+s[high]
                low-=1
                high+=1
            if len(cur)>len(ans):
                ans = cur
        
        return ans