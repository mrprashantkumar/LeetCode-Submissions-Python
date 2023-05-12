class Solution:
    def reverseWords(self, s: List[str]) -> None:
        def reverse(s, start, end):
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
        
        n = len(s)
        reverse(s, 0, n-1)
        
        i, j = 0, 0
        while i < n:
            while j < n and s[j] != ' ':
                j += 1
            
            reverse(s, i, j-1)
            i = j+1
            j = i+1