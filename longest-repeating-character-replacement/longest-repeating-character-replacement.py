class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        d = {}
        left = 0

        for right in range(n):
            d[s[right]] = d.get(s[right], 0) + 1
            
            while right - left - max(d.values()) >= k:
                d[s[left]] -= 1
                left += 1
            
            ans = max(ans, right-left+1)
            # print(left, right, ans, d)
        return ans