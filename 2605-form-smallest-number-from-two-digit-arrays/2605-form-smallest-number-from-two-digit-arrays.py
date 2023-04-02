class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        s1, s2 = set(nums1), set(nums2)
        
        for i in range(1, 10):
            if i in s1 and i in s2:
                return i
        
        a1 = min(s1)*10 + min(s2)
        a2 = min(s2)*10 + min(s1)
        return min(a1, a2)