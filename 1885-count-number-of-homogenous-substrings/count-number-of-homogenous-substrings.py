class Solution:
    def countHomogenous(self, s: str) -> int:
        ans = 0
        last = ''
        count = 0
        for i in s:
            if i == last:
                count += 1
            else:
                count = 1
                last = i
            
            ans += count
            ans %= 1000000007
        
        return ans