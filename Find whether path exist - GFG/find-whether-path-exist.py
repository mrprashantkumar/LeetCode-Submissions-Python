from collections import *

class Solution:
    
    #Function to find whether a path exists from the source to destination.
	def is_Possible(self, grid):
	    def isvalid(p, q):
	        return 0<=p<n and 0<=q<m and grid[p][q] in [2, 3] and (p, q) not in visited
	        
		n, m = len(grid), len(grid[0])
		for i in range(n):
		    for j in range(m):
		        if grid[i][j] == 1:
		            src = (i, j)
		        if grid[i][j] == 2:
		            dest = (i, j)
		
		visited = set()
		qu = deque([(src)])
		while qu:
		    x, y = qu.popleft()
		    if dest == (x, y):
		        return True
		        
		    visited.add((x, y))
		    for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
		        if isvalid(x+dx, y+dy):
		            visited.add((x+dx, y+dy))
		            qu.append((x+dx, y+dy))
		
		return False

#{ 
 # Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		grid = []
		for _ in range(n):
			a = list(map(int, input().split()))
			grid.append(a)
		obj = Solution()
		ans = obj.is_Possible(grid)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends