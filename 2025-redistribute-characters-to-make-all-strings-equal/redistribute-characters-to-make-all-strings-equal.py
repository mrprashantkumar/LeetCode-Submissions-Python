class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)
        if n == 1:
            return True
        
        d = {}
        for word in words:
            for char in word:
                d[char] = d.get(char, 0) + 1
        
        for key in d:
            if d[key]%n != 0:
                return False
        return True