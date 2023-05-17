#User function template for Python

class Solution:
	def shortest_distance(self, matrix):
	    n = len(matrix)
	    for i in range(n):
            for j in range(n):
                if matrix[i][j] == -1:
                    matrix[i][j] = 1000000007
                if i == j:
                    matrix[i][j] = 0
	                
	    for via in range(n):
	        for i in range(n):
	            for j in range(n):
	                matrix[i][j] = min(matrix[i][via]+matrix[via][j], matrix[i][j])
	   
	    for i in range(n):
            for j in range(n):
                if matrix[i][j] >= 1000000007:
                    matrix[i][j] = -1
		#Code here


#{ 
 # Driver Code Starts
#Initial template for Python 

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		matrix = []
		for _ in range(n):
			matrix.append(list(map(int, input().split())))
		obj = Solution()
		obj.shortest_distance(matrix)
		for _ in range(n):
			for __ in range(n):
				print(matrix[_][__], end = " ")
			print()
# } Driver Code Ends