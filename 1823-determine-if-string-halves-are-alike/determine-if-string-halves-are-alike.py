class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = {'a','e','i','o','u','A','E','I','O','U'}
        
        l, r = 0, len(s)-1
        a, b = 0, 0

        while l<r:
            if s[l] in vowels:
                a+=1
            if s[r] in vowels:
                b+=1
            
            l+=1
            r-=1
        
        return a==b