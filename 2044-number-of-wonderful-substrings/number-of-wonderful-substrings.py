class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        d = {0:1}
        mask, ans = 0, 0
        
        for c in word:
            val = ord(c) - 97
            mask ^= (1 << val)

            if mask in d:
                ans += d[mask]
                d[mask] += 1
            else:
                d[mask] = 1
            
            for i in range(10):
                m = mask ^ (1 << i)
                if m in d:
                    ans += d[m]
        
        return ans