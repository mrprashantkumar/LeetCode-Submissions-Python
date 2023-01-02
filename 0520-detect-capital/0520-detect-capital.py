class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper() or word.islower():
            return True
        elif word[0].isupper() and word[1:].islower():
            return True
        return False