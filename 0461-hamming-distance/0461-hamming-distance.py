class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        b1, b2 = [0]*32, [0]*32
        
        for i in range(32):
            b1[i] = x%2
            x //= 2
            b2[i] = y%2
            y //= 2
        
        ans = 0
        for i, j in zip(b1, b2):
            ans += int(i != j)
        return ans