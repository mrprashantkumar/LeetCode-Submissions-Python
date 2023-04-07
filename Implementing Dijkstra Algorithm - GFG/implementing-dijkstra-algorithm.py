from collections import *
import heapq
class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, src):
        ans = [1000000007]*V
        ans[src] = 0
        
        qu = set()
        qu.add((0, src))
        while qu:
            x, curr = qu.pop()
            for nei, wt in adj[curr]:
                if ans[nei] > ans[curr]+wt:
                    if (ans[nei], nei) in qu:
                        qu.remove((ans[nei], nei))
                    ans[nei] = ans[curr]+wt
                    qu.add((ans[nei], nei))
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends