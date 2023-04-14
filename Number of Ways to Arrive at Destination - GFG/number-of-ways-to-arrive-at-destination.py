#User function Template for python3
#User function Template for python3

from typing import List
from collections import defaultdict
import sys, heapq

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj = [[] for i in range(n)]
        
        for it in roads:
            adj[it[0]].append([it[1], it[2]])
            adj[it[1]].append([it[0], it[2]])
        
        dist = [10000000000]*n
        ways = [0]*n
        
        dist[0] = 0
        ways[0] = 1
        pq = [(0, 0)]
        
        mod = 1000000007
        
        while pq:
            dis, node = heapq.heappop(pq)
            
            for adjNode, edW in adj[node]:
                if (dis + edW < dist[adjNode]):
                    dist[adjNode] = dis + edW
                    heapq.heappush(pq, (dis + edW, adjNode))
                    ways[adjNode] = ways[node]
                    
                elif (dis + edW == dist[adjNode]):
                    ways[adjNode] = (ways[adjNode] + ways[node]) % mod
                    
        return ways[n - 1] % mod


#{ 
 # Driver Code Starts
#Initial Template for Python 3

class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n,m=map(int,input().split())
        
        
        adj=[]
        
        for i in range(m):
            tmp =[]
            x,y,z=map(int,input().split())
            tmp.append(x)
            tmp.append(y)
            tmp.append(z)
            adj.append(tmp)
            
        
        
        
       
        obj = Solution()
        res = obj.countPaths(n, adj)
        
        print(res)
        

# } Driver Code Ends