class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        d1, d2 = Counter(words1), Counter(words2)
        ans = 0
        for i in d1:
            if d1[i] == d2[i] == 1:
                ans += 1
        return ans