class Solution:
    def validPalindrome(self, s: str) -> bool:
        def helper(low, high, used):
            if low >= high:
                return True
            
            if s[low] == s[high]:
                return helper(low+1, high-1, used)
            else:
                if used:
                    return False
                else:
                    return max(helper(low+1, high, not used), helper(low, high -1, not used))
        
        return helper(0, len(s)-1, False)