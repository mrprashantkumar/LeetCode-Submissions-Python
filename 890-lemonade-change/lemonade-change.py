class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        d = Counter()
        for i in bills:
            if i == 5:
                d[i] += 1
            elif i == 10:
                if d[5] >= 1:
                    d[5] -= 1
                    d[i] += 1
                else:
                    return False
            else:
                if d[5] >= 1 and d[10] >= 1:
                    d[5] -= 1
                    d[10] -= 1
                    d[i] += 1
                elif d[5] >= 3:
                    d[5] -= 3
                    d[i] += 1
                else:
                    return False

        return True