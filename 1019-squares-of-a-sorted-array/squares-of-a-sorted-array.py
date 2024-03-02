class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        low, high = 0, len(nums)-1
        ans = []
        
        while low <= high:
            if abs(nums[low]) > abs(nums[high]):
                ans.append(nums[low]*nums[low])
                low += 1
            else:
                ans.append(nums[high]*nums[high])
                high -= 1

        return ans[::-1]