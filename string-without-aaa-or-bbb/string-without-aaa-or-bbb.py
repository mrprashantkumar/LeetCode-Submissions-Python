class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        ans = ''
        while a >= 0 and b >= 0:
            if a > b:
                if (a-b) > 2:
                    ans += 'aab'
                    b -= 1
                    a -= 2
                else:
                    ans += 'a'
                    a -= 1
            elif b > a:
                if (b-a) > 2:
                    ans += 'bba'
                    b -= 2
                    a -= 1
                else:
                    ans += 'b'
                    b -= 1
            else:
                if ans and ans[-1] == 'a':
                    ans += 'ba'*b
                else:
                    ans += 'ab'*b
                a, b = -1, -1
        return ans