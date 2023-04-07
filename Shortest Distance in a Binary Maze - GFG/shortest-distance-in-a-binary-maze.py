#User function Template for python3

from typing import List
from collections import *
class Solution:
    def shortestPath(self, grid: List[List[int]], src: List[int], dest: List[int]) -> int:
        def check(p, q):
            return 0<=p<n and 0<=q<m and grid[p][q] == 1 and (p, q) not in visited
        if src == dest:
            return 0
        visited = set()
        qu = deque([src])
        ans = 0
        while qu:
            l = len(qu)
            for _ in range(l):
                x, y = qu.popleft()
                for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                    if check(x+dx, y+dy):
                        if [x+dx, y+dy] == dest:
                            return ans+1
                        visited.add((x+dx, y+dy))
                        qu.append((x+dx, y+dy))
            
            ans += 1
            
        return -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

         
if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().strip().split())
        grid=[]
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        source = [0] * 2
        source[0], source[1] = map(int,input().strip().split())
        destination = [0] * 2
        destination[0], destination[1] = map(int,input().strip().split())
        obj=Solution()
        print(obj.shortestPath(grid, source, destination))
# } Driver Code Ends