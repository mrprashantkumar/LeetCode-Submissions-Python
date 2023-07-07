class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        c = 0
        left = 0
        count1, count0 = 0, 0
        for i in range(n):
            if nums[i] == 0:
                count0 += 1
            else:
                count1 += 1
            
            while count0 > k:
                if nums[left] == 0:
                    count0 -= 1
                else:
                    count1 -= 1
                left += 1
            
            ans = max(ans, count0+count1)
        return ans