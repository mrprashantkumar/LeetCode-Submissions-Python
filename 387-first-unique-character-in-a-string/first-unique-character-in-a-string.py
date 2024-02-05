class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = Counter(s)
        for i,x in enumerate(s):
            if d[x] == 1:
                return i
        return -1