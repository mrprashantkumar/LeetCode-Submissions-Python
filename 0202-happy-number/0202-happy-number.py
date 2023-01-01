class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            if n==1:
                return True
            seen.add(n)
            n = sum([int(i)*int(i) for i in str(n)])
            if n in seen:
                return False