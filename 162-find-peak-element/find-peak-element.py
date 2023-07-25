class Solution:
    def findPeakElement(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 0
        arr = [-10000000007] + arr + [-10000000007]
        left, right = 1, n
        while left <= right:
            mid = (left+right)//2
            if arr[mid-1]<arr[mid]>arr[mid+1]:
                return mid-1
            elif arr[mid-1]<arr[mid]<arr[mid+1]:
                left = mid+1
            else:
                right = mid-1