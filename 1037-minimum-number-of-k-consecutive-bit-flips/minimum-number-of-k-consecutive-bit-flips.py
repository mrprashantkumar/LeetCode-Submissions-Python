class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        isFlipped = [0]*n
        flipped, ans = 0, 0
        for i in range(n):
            if i >= k:
                flipped ^= isFlipped[i-k]
            
            if flipped == nums[i]:
                if (i+k > n):
                    return -1
                
                isFlipped[i] = 1
                flipped ^= 1
                ans += 1
        
        return ans