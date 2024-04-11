class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        seen = []
        for i in num:
            while seen and k and seen[-1]>i:
                seen.pop()
                k-=1
            
            if seen or i != '0':
                seen.append(i)
        
        if k>0:
            seen = seen[:-k]
        return "".join(seen) or '0'