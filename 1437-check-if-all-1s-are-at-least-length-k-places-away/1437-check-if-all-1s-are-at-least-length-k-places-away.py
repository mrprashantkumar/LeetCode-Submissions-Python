class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last = -10000007
        for i,x in enumerate(nums):
            if x == 1:
                if i - last <= k:
                    return False
                last = i
        return True