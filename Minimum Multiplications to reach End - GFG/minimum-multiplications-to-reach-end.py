#User function Template for python3

from typing import List
from collections import *
class Solution:
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        m = 100000
        visited = set()
        qu = deque([start])
        visited.add(start)
        
        ans = 0
        while qu:
            l = len(qu)
            for _ in range(l):
                curr = qu.popleft()
                for ele in arr:
                    val = (ele*curr) % m
                    if val == end:
                        return ans+1
                    if val not in visited:
                        visited.add(val)
                        qu.append(val)
            ans += 1
        
        return -1
                
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        start, end = list(map(int,input().split()))
        obj=Solution()
        print(obj.minimumMultiplications(arr, start, end))
# } Driver Code Ends