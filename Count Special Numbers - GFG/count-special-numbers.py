#User function Template for python3
from collections import *
class Solution:
    def countSpecialNumbers(self, N, arr):
        arr.sort()
        d=Counter(arr)
        c=0
        for i in range(N):
            if d[arr[i]]>1:
                c+=1
            else:
                for j in range(i):
                    if arr[i]%arr[j]==0:
                        c+=1
                        break
                    j+=1
        return c


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    
    T = int(input())
    while T > 0: 
        N=int(input())
        arr = [int(i) for i in input().split()]
        ob = Solution()
        print(ob.countSpecialNumbers(N, arr))
        
        T -= 1
# } Driver Code Ends