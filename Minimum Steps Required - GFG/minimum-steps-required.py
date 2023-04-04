class Solution:
    def minSteps(self, s : str) -> int:
        ca, cb = 0, 0
        n = len(s)
        i = 0
        while i<n:
            c = s[i]
            while i<n and s[i] == c:
                i += 1
            
            if c=='a':
                ca += 1
            else:
                cb += 1
        
        # print(ca, cb)
        
        return min(ca, cb) + 1

#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        str = (input())
        
        obj = Solution()
        res = obj.minSteps(str)
        
        print(res)
        

# } Driver Code Ends