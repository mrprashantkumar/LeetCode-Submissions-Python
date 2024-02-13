class Solution:
    def minTimeToType(self, word: str) -> int:
        curr = 'a'
        ans = 0
        for ch in word:
            diff = abs(ord(ch) - ord(curr))
            ans +=  (1 + min(diff, 26 - diff))
            curr = ch
        return ans