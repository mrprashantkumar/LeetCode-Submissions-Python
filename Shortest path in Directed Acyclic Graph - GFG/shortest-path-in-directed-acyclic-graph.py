#User function Template for python3
from collections import *
from typing import List

class Solution:
    def shortestPath(self, n : int, m : int, edges : List[List[int]]) -> List[int]:
        def dfs(node):
            visited.add(node)
            for nei, wt in graph[node]:
                if nei not in visited:
                    dfs(nei)
            topo.append(node)
            return False
            
        graph = defaultdict(list)
        for src, des, wt in edges:
            graph[src].append([des, wt])
        
        visited = set()
        topo = []
        for i in range(n):
            if i not in visited:
                dfs(i)
        
        ans = [1000000007]*n
        ans[0] = 0
        while topo:
            curr = topo.pop()
            for dest, wt in graph[curr]:
                dist = ans[curr]+wt
                if dist < ans[dest]:
                    ans[dest] = dist
        
        for i in range(n):
            if ans[i] == 1000000007:
                ans[i] = -1
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

from typing import List




class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()



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
        
        
        edges=IntMatrix().Input(m, 3)
        
        obj = Solution()
        res = obj.shortestPath(n, m, edges)
        
        IntArray().Print(res)
# } Driver Code Ends