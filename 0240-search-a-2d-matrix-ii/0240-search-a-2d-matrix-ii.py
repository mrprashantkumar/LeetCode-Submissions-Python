class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def bs(arr, start, end, target):
            while start<=end:
                mid = (start+end)//2
                if arr[mid] == target:
                    return True
                elif arr[mid] > target:
                    end  = mid-1
                else:
                    start = mid+1
            return False
        
        m = len(matrix[0])
        for arr in matrix:
            ans = bs(arr, 0, m-1, target)
            if ans:
                return True
        return False