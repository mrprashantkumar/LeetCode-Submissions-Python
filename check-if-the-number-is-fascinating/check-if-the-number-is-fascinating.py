class Solution:
    def isFascinating(self, n: int) -> bool:
        s = str(n)
        s += str(n*2)
        s += str(n*3)
        return ''.join(sorted(s)) == '123456789'