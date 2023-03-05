class Solution:
    def splitNum(self, num: int) -> int:
        arr = sorted(str(num))
        # print(arr)
        n = len(arr)
        num1, num2 = 0, 0
        for i, x in enumerate(arr):
            if i&1:
                num2 = (num2*10 + int(x))
            else:
                num1 = (num1*10 + int(x))
            # print(num1, num2)
        return num1+num2