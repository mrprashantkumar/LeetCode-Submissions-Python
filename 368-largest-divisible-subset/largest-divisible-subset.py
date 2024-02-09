class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        dp = defaultdict(lambda : 1)
        prev = defaultdict(lambda : -1)
        maxlen = 0
        endval = 0
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    dp[nums[i]] = max(dp[nums[i]], 1+dp[nums[j]])
                    if dp[prev[nums[i]]] <= dp[nums[j]]:
                        prev[nums[i]] = nums[j]
                    if dp[nums[i]] > maxlen:
                        maxlen = dp[nums[i]]
                        endval = nums[i]

        ans = []
        while prev[endval] != -1:
            ans.append(endval)
            endval = prev[endval]
        ans.append(endval)
        if maxlen == 0:
            return [nums[0]]
        return ans