class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        lenstr = 0
        for ch in s:
            if ch.isdigit():
                lenstr *= int(ch)
            else:
                lenstr += 1
        
        for ch in s[::-1]:
            k %= lenstr
            if k == 0 and ch.isalpha():
                return ch
            
            if ch.isdigit():
                lenstr /= int(ch)
            else:
                lenstr -= 1