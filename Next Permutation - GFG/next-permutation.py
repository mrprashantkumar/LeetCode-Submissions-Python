#User function Template for python3

class Solution:
    def nextPermutation(self, n, arr):
        i = n-2
        
        while i >= 0:
            if arr[i] >= arr[i+1]:
                i -= 1
            else:
                break
        
        if i == n-2:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            return arr
        
        if i == -1:
            arr.reverse()
            return arr
        
        j = i+1
        nextGreaterInd = j
        while j < n:
            if arr[i] < arr[j] and arr[j] < arr[nextGreaterInd]:
                nextGreaterInd = j
            j += 1
        
        arr[i], arr[nextGreaterInd] = arr[nextGreaterInd], arr[i]
        
        low, high = i+1, n-1
        while low <= high:
            arr[low], arr[high] = arr[high], arr[low]
            low += 1
            high -= 1
        
        return arr
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        ans = ob.nextPermutation(N, arr)
        for i in range(N):
            print(ans[i],end=" ")
        print()
# } Driver Code Ends