# User function Template for python3

class Solution:
    #Function to find equilibrium point in the array.
    def equalSum(self,A, N):
        # Your code here
        suff = [0]*(N+1)
        
        for i in range(N-1, -1, -1):
            suff[i] = A[i]+suff[i+1]
        
        # print(suff)
        pref = 0
        for i in range(N):
            if pref == suff[i+1]:
                return i+1
            pref += A[i]
        return -1
            
#{ 
 # Driver Code Starts
# Initial Template for Python 3

import math


def main():

    T = int(input())

    while(T > 0):

        N = int(input())

        A = [int(x) for x in input().strip().split()]
        ob=Solution()

        print(ob.equalSum(A, N))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends