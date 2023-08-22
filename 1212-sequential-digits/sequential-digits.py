class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        nums = '123456789'
        for l in range(2, 10):
            for i in range(10-l):
                n = int(nums[i:i+l])
                if low <= n <= high:
                    ans.append(n)
        return ans