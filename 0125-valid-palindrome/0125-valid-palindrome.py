class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ""
        for i in s:
            if i.isalpha() or i.isdigit():
                st += i.lower()
        return st==st[::-1]