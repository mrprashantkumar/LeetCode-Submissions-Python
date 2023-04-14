#User function Template for python3
from typing import List
from collections import *
import heapq
class Solution:
    def CheapestFLight(self,n,flights,src,dst,k):
        graph = defaultdict(list)
        for i, j, w in flights:
            graph[i].append((j, w))
        
        visited = {}
        qu = [(0, 0, src)]
        
        while qu:
            cost, stops, node = heapq.heappop(qu)
            if node == dst and stops-1 <= k:
                return cost
            
            if node not in visited or visited[node] > stops:
                visited[node] = stops
                for nei, wt in graph[node]:
                    heapq.heappush(qu, (cost + wt, stops + 1, nei))
                
        return -1
    
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    test_cases = int(input())
    for _ in range (test_cases):
        n,edge=map(int,input().split())
        flights=[]
        for _ in range(edge):
            temp=list(map(int,input().split()))
            flights.append(temp[:])
        src=int(input())
        dst=int(input())
        k=int(input())
        obj=Solution()
        res=obj.CheapestFLight(n,flights,src,dst,k)
        print(res)

        
        
# } Driver Code Ends