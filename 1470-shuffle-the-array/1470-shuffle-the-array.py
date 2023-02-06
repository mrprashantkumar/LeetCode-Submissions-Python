class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        i, j = 0, n
        
        ans = []
        for k in range(2*n):
            if k&1:
                ans.append(nums[j])
                j += 1
            else:
                ans.append(nums[i])
                i += 1
        return ans