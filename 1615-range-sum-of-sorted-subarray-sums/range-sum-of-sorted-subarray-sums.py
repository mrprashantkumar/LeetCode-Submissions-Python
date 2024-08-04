class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        subarraySum = []
        for i in range(n):
            curr = 0
            for j in range(i, n):
                curr += nums[j]
                subarraySum.append(curr)

        subarraySum.sort()
        ans = 0
        for i in range(left-1, right):
            ans += subarraySum[i]
            ans %= 1000000007
        return ans