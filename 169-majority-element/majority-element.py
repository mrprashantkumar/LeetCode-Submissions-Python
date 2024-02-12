class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        c = 0
        for i in range(n):
            if c==0:
                ans = nums[i]
                c+=1
            elif nums[i]==ans:
                c+=1
            else:
                c-=1
        return ans