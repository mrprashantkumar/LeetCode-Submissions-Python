#User function Template for python3

class Solution:
	def closedIslands(self, matrix, n, m):
	    def isvalid(p, q):
	        return 0<=p<n and 0<=q<m and (p, q) not in visited and matrix[p][q] == 1
	        
		def dfs(x, y):
		    visited.add((x, y))
		    for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
		        if isvalid(x+dx, y+dy):
		            dfs(x+dx, y+dy)
		
		visited = set()
		for i in range(n):
		    if matrix[i][0] == 1:
		        visited.add((i, 0))
		        dfs(i, 0)
		    if matrix[i][m-1] == 1:
		        visited.add((i, m-1))
		        dfs(i, m-1)
		
		for j in range(m):
		    if matrix[0][j] == 1:
		        visited.add((0, j))
		        dfs(0, j)
		    if matrix[n-1][j] == 1:
		        visited.add((n-1, j))
		        dfs(n-1, j)
		
		ans = 0
		for i in range(1, n-1):
		    for j in range(1, m-1):
		        if isvalid(i, j):
		            dfs(i, j)
		            ans += 1
		return ans
		    
		        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
		
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N, M = map(int,input().split())
        matrix = []
        for i in range(N):
            nums = list(map(int,input().split()))
            matrix.append(nums)
        obj = Solution()
        print(obj.closedIslands(matrix, N, M))
# } Driver Code Ends