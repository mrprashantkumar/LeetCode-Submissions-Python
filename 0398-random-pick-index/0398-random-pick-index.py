class Solution:

    def __init__(self, nums: List[int]):
        self.d = defaultdict(list)
        for i, x in enumerate(nums):
            self.d[x].append(i)

    def pick(self, target: int) -> int:
        n = len(self.d[target])
        r = int(random.random() * n)
        return self.d[target][r]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)