class Solution:
    def makeGood(self, s: str) -> str:
        seen = []
        
        for i in s:
            if seen and abs(ord(seen[-1])-ord(i)) == 32:
                seen.pop()
            else:
                seen.append(i)
        
        return "".join(seen)