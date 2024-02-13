class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        d = Counter()
        lens = []
        for word in words:
            d += Counter(word)
            lens.append(len(word))

        pairs = sum(i//2 for i in d.values())
        lens.sort()
        ans = 0
        for l in lens:
            pairs -= l//2
            ans += pairs >= 0
        return ans