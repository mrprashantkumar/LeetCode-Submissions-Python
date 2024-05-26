class Solution:
    def checkRecord(self, s: str) -> bool:
        last = ''
        a, l = 0, 0
        for i in s:
            if i == 'A':
                a += 1
                l = 0
            elif i == 'L':
                l += 1
            else:
                l = 0
            
            last = i
            if a >= 2 or l >= 3:
                return False
            
        return True