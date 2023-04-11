#User function Template for python3

class Solution():
    def solve(self, a, b, c):
        arr = [a, b, c]
        arr.sort()
        mini, mid, maxi = tuple(arr)
        if maxi > (mini+mid+1)*2:
            return -1
        return sum(arr)
        
        #your code goes here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import Counter
for _ in range(int(input())):
    a, b, c=map(int,input().split())
    obj = Solution()
    res = obj.solve(a, b, c)
    
    print(res)
# } Driver Code Ends