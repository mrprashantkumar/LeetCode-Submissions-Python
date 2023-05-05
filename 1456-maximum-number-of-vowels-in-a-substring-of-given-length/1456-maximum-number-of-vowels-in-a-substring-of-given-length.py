class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        vowels = 'aeiou'
        ans = 0
        c = 0
        for i in range(k):
            c += int(s[i] in vowels)
        
        for i in range(n-k):
            ans = max(ans, c)
            c -= int(s[i] in vowels)
            c += int(s[i+k] in vowels)
            # print(s[i], s[i+k])
        ans = max(ans, c)
        return ans