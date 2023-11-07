class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n = len(dist)
        nums = [i/j for i, j in zip(dist, speed)]
        nums.sort()

        ans = 0
        for i in range(n):
            if nums[i] > i:
                ans = i+1
            else:
                break
        return ans