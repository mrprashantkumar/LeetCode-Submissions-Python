class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = -1005
        curprod = 1
        for i in nums:
            curprod *=i
            ans = max(ans, curprod)
            if i==0:
                curprod = 1
                
        curprod = 1
        for i in nums[::-1]:
            curprod *= i
            ans = max(ans, curprod)
            if i==0:
                curprod = 1
                
        return ans