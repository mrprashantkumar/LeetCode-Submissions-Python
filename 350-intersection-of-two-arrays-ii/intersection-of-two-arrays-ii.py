class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = Counter(nums1) & Counter(nums2)
        return d.elements()