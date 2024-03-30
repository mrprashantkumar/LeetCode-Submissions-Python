class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        c1, c2 = 0, 0
        n = len(nums)

        # find count of SubArrays with At Most K Distinct Elements
        d = Counter()
        left = 0
        for right in range(n):
            d[nums[right]] += 1
            while len(d) > k:
                d[nums[left]] -= 1
                if d[nums[left]] == 0:
                    del d[nums[left]]
                left += 1
            
            c1 += (right - left + 1)
        

        # find count of SubArrays with At Most K-1 Distinct Elements
        d = Counter()
        left = 0
        for right in range(n):
            d[nums[right]] += 1
            while len(d) > k-1: # change line
                d[nums[left]] -= 1
                if d[nums[left]] == 0:
                    del d[nums[left]]
                left += 1
            
            c2 += (right - left + 1)
        
        return c1 - c2