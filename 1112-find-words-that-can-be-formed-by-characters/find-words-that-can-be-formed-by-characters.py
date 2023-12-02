class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        def helper(s):
            curr = Counter(s)
            for c in s:
                if curr[c] > count[c]:
                    return False
            return True
        
        count = Counter(chars)
        ans = 0
        for word in words:
            if helper(word):
                ans += len(word)
        return ans