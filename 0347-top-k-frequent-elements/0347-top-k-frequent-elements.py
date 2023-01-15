class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        arr = sorted(d, key = d.get, reverse = True)
        return arr[:k]