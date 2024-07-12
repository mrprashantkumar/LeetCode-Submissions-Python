class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def removeAB(s):
            seen = []
            for i in s:
                if i == 'b':
                    if seen and seen[-1] == 'a':
                        seen.pop()
                        self.ans += x
                    else:
                        seen.append(i)
                else:
                    seen.append(i)
            
            return "".join(seen)
        
        def removeBA(s):
            seen = []
            for i in s:
                if i == 'a':
                    if seen and seen[-1] == 'b':
                        seen.pop()
                        self.ans += y
                    else:
                        seen.append(i)
                else:
                    seen.append(i)
            
            return "".join(seen)
        
        self.ans = 0
        if x > y:
            s = removeAB(s)
            removeBA(s)
        else:
            s = removeBA(s)
            removeAB(s)
        return self.ans