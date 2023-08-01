class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        def isvalid(p):
            return 0<=p<arrLen
        
        def helper(i, count):
            if count == steps:
                return int(i==0)
            
            if (i, count) in dp:
                return dp[(i, count)]

            stay = helper(i, count+1)
            left, right = 0, 0
            if isvalid(i-1):
                left = helper(i-1, count+1)
            if isvalid(i+1):
                right = helper(i+1, count+1)
            
            dp[(i, count)] = (stay+left+right)%1000000007
            return dp[(i, count)]
        
        dp = {}
        return helper(0, 0)