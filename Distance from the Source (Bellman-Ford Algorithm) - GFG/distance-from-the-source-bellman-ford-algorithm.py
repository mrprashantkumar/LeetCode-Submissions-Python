#User function Template for python3
from collections import *
import heapq
class Solution:
    # Function to construct and return cost of MST for a graph
    # represented using adjacency matrix representation
    '''
    V: nodes in graph
    edges: adjacency list for the graph
    S: Source
    '''
    def bellman_ford(self, V, edges, src):
        ans = [100000000]*V
        ans[src] = 0
        
        for _ in range(V-1):
            for i, j, wt in edges:
                if ans[i]+wt < ans[j]:
                    ans[j] = ans[i]+wt
        
        for i, j, wt in edges:
            if ans[i]+wt < ans[j]:
                return [-1]
        
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
        edges = []
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            edges.append([u,v,w])
        S=int(input())
        ob = Solution()
        
        res = ob.bellman_ford(V,edges,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends