from collections import *
class Solution:
	def floodFill(self, image, sr, sc, newColor):
	    n, m = len(image), len(image[0])
	    initial = image[sr][sc]
	    
	    def check(p, q):
	        return 0<=p<n and 0<=q<m and image[p][q] == initial and not visited[p][q]
	        
	        
	    def dfs(x, y):
	        visited[x][y] = True
	        image[x][y] = newColor
	        for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
	            if check(x+dx, y+dy):
	                dfs(x+dx, y+dy)
	    
	    visited = [[False]*m for _ in range(n)]
	    dfs(sr, sc)
	    return image
	    
	    


#{ 
 # Driver Code Starts
import sys
sys.setrecursionlimit(10**7)
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n)
		m = int(m)
		image = []
		for _ in range(n):
			image.append(list(map(int, input().split())))
		sr, sc, newColor = input().split()
		sr = int(sr); sc = int(sc); newColor = int(newColor);
		obj = Solution()
		ans = obj.floodFill(image, sr, sc, newColor)
		for _ in ans:
			for __ in _:
				print(__, end = " ")
			print()
# } Driver Code Ends