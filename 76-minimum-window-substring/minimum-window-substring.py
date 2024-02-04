class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ds, dt = Counter(), Counter(t)
        n = len(s)
        ans = []
        
        left = 0
        for right in range(n):
            ds[s[right]] += 1            
            if ds & dt != dt:
                continue
            
            while left <= right:
                ds[s[left]] -= 1 
                left += 1
                if ds & dt == dt:
                    continue
                ans.append(s[left-1:right+1])
                break
        
        if not ans:
            return ""        
        return min(ans, key=len)