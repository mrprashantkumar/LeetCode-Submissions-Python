class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        m = 0
        arr = defaultdict(list)

        for i in range(n):
            for j, x in enumerate(nums[i]):
                m = max(m, j)
                arr[i+j].append(x)

        ans = []
        for i in range(n+m):
            ans += arr[i][::-1]
        return ans