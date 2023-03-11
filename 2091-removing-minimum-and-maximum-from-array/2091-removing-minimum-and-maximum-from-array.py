class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        mini, maxi = 1000000007, -1000000007
        miniInd, maxiInd = 0, 0
        n = len(nums)
        for i, x in enumerate(nums):
            if x<mini:
                mini = x
                miniInd = i
            if x>maxi:
                maxi = x
                maxiInd = i
        # print(miniInd, maxiInd)
        return min(miniInd+n-maxiInd+1, maxiInd+n-miniInd+1, max(miniInd, maxiInd)+1, n-min(miniInd, maxiInd))