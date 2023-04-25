class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)
        if len(words) == 1:
            return True
        
        c = 0
        d = {}
        for word in words:
            for char in word:
                d[char] = d.get(char, 0) + 1
                c = d[char]
        
        for key in d:
            if d[key]%n != 0:
                return False
        return True