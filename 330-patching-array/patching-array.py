class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        l = len(nums)
        right, i = 0, 0
        ans = 0
        # added = []
        while right < n:
            if i >= l or right+1 < nums[i]:
                ans += 1
                # added.append(right+1)
                right += (right+1)
            else:
                right += nums[i]
                i += 1
            
            if right >= n:
                break
        # print(added)
        return ans