class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a, b = 0, int(sqrt(c))+1

        while a <= b:
            val = a*a + b*b
            if val == c:
                return True
            elif val > c:
                b -= 1
            else:
                a += 1
        return False