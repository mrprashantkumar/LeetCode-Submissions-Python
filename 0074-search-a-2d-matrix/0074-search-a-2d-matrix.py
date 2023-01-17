class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        
        low, high = 0, m*n - 1
        
        while low<=high:
            mid = (low+high)//2
            midval = matrix[mid//n][mid%n]
            
            if midval == target:
                return True
            elif midval > target:
                high = mid-1
            else:
                low = mid+1
        
        return False