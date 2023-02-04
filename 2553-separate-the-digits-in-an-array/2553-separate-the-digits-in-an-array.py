class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            ans += [int(i) for i in str(i)]
        return ans