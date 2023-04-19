class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        seen = set()
        c = ""
        for i in word:
            if i.isdigit():
                c += i
            else:
                if c: seen.add(int(c))
                c = ""
        if c: seen.add(int(c))
        return len(seen)