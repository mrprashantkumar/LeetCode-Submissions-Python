class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n, k = len(nums), len(set(nums))
        ans = 0
        d = defaultdict(int)
        i = 0
        for j in range(n):
            d[nums[j]] += 1

            while len(d) == k:
                d[nums[i]] -= 1
                if d[nums[i]] == 0:
                    del d[nums[i]]
                i += 1
            ans += i
        return ans