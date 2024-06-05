class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ans = Counter(words[0])
        for word in words:
            ans &= Counter(word)
        return ans.elements()