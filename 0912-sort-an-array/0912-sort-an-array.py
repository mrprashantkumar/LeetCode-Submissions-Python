class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr1, arr2):
            n, m = len(arr1), len(arr2)
            i, j = 0, 0
            ans = []
            while i<n and j<m:
                if arr1[i]<=arr2[j]:
                    ans.append(arr1[i])
                    i += 1
                else:
                    ans.append(arr2[j])
                    j += 1
            
            while i<n:
                ans.append(arr1[i])
                i += 1
            
            while j<m:
                ans.append(arr2[j])
                j += 1
            
            return ans
        
        def mergesort(arr):
            n = len(arr)
            if n<=1:
                return arr
            
            start, end = 0, n
            mid = (start+end)//2
            arr1 = mergesort(arr[start:mid])
            arr2 = mergesort(arr[mid:end])
            return merge(arr1, arr2)
        
        return mergesort(nums)