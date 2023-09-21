class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = nums1 + nums2
        arr.sort()
        l = len(arr)
        i = l//2
        
        if l%2 == 0:
            return (arr[i-1] + arr[i])/2
        else:
            return arr[i]