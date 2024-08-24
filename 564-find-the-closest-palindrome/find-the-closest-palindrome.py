class Solution:
    def nearestPalindromic(self, n: str) -> str:
        l = len(n)
        half = l//2 if l&1 else l//2 - 1
        s = int(n[:half+1])
        nums = []
        if l&1:
            nums.append(int(str(s) + str(s)[-2::-1]))
            s -= 1
            nums.append(int(str(s) + str(s)[-2::-1]))
            s += 2
            nums.append(int(str(s) + str(s)[-2::-1]))
        else:
            nums.append(int(str(s) + str(s)[::-1]))
            s -= 1
            nums.append(int(str(s) + str(s)[::-1]))
            s += 2
            nums.append(int(str(s) + str(s)[::-1]))
        nums.append(10 ** (l-1) - 1)
        nums.append(10 ** l + 1)

        res, diff = "", inf
        for i in nums:
            if i == int(n):
                continue
            if diff > abs(int(n) - i):
                res = i
                diff = abs(int(n) - i)
            elif diff == abs(int(n) - i):
                res = min(res, i)
        return str(res)