class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        n = len(word)
        ans = [0] * n
        pref = 0
        for i in range(n):
            pref = (pref * 10 + int(word[i])) % m
            if pref == 0:
                ans[i] = 1
        return ans