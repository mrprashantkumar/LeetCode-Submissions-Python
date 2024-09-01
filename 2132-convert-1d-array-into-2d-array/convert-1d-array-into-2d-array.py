class Solution:
    def construct2DArray(self, nums: List[int], m: int, n: int) -> List[List[int]]:
        l = len(nums)
        if l != m*n:
            return []
        
        ans = [[0] * n for _ in range(m)]
        k = 0
        for i in range(m):
            for j in range(n):
                ans[i][j] = nums[k]
                k += 1
        return ans