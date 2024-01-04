class Solution:
    def minOperations(self, nums: List[int]) -> int:
        d = Counter(nums)
        ans = 0
        
        for i in d:
            if d[i] == 1:
                return -1
            ans += (d[i]+2)//3
        
        return ans