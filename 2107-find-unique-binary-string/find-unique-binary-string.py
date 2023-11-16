class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        def getint(s):
            num = 0
            i = 0
            for c in s[::-1]:
                num += 2**i * int(c)
                i += 1
            return num
        
        n = len(nums)
        vals = [getint(i) for i in nums]

        for i in range(n+3):
            if i not in vals:
                ans = ''
                while n:
                    n -= 1
                    ans = str(i%2) + ans
                    i //= 2
                return ans