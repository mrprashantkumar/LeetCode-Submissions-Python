class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in nums:
            if nums[abs(i)-1]<0:
                ans.append(abs(i))
            else:
                nums[abs(i)-1] = -nums[abs(i)-1]
        return ans