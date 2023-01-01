class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        if k<=9 and any(int(i)>k for i in s):
            return -1
        
        ans=0
        i=0
        n = len(s)
        while i<n:
            curr = 0
            while i<n and curr<=k:
                curr = curr*10 + int(s[i])
                i+=1
                if curr>k:
                    i-=1
                    break
            ans+=1
        
        return ans