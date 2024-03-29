class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        nums1.sort()
        nums2.sort()

        for i in nums1:
            d = Counter(nums2)
            low, high = 0, len(nums2)-1
            while low < high:
                p = nums2[low] * nums2[high]
                if p == i*i:
                    if nums2[low] == nums2[high]:
                        ans += d[nums2[low]] * (d[nums2[low]] - 1) // 2
                    else:
                        ans += d[nums2[low]] * d[nums2[high]]
                    val1, val2 = nums2[low], nums2[high]
                    while low <= high and nums2[low] == val1:
                        low += 1
                    while low <= high and nums2[high] == val2:
                        high -= 1
                elif p < i*i:
                    low += 1
                else:
                    high -= 1
        

        for i in nums2:
            d = Counter(nums1)
            low, high = 0, len(nums1)-1
            while low < high:
                p = nums1[low] * nums1[high]
                if p == i*i:
                    if nums1[low] == nums1[high]:
                        ans += d[nums1[low]] * (d[nums1[low]] - 1) // 2
                    else:
                        ans += d[nums1[low]] * d[nums1[high]]
                    val1, val2 = nums1[low], nums1[high]
                    while low <= high and nums1[low] == val1:
                        low += 1
                    while low <= high and nums1[high] == val2:
                        high -= 1
                elif p < i*i:
                    low += 1
                else:
                    high -= 1
        
        return ans