class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.d1 = Counter(nums1)
        self.d2 = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        self.d2[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.d2[self.nums2[index]] += 1
        

    def count(self, tot: int) -> int:
        ans = 0
        for i in self.d1:
            if tot-i in self.d2:
                ans += self.d1[i]*self.d2[tot-i]
        return ans


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)