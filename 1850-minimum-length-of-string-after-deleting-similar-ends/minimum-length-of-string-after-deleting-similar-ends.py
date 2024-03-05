class Solution:
    def minimumLength(self, s: str) -> int:
        low, high = 0, len(s)-1

        while low <= high:
            if low == high:
                return 1
            if s[low] == s[high]:
                ch = s[low]
                while low <= high and s[low] == ch:
                    low += 1
                
                while low <= high and s[high] == ch:
                    high -= 1
            else:
                break
            
        if low >= high:
            return 0
        return high-low+1