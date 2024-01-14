class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        n1, n2 = len(word1), len(word2)
        if n1 != n2:
            return False
        
        d1, d2 = Counter(word1), Counter(word2)
        
        return set(word1) == set(word2) and sorted(d1.values()) == sorted(d2.values())