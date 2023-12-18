class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def getdivisors(n):
            count = 0
            total = 0
            r = int(sqrt(n))
            for i in range(1, r+1):
                if n % i == 0:
                    total += i
                    if i == (n//i):
                        return 0
                    total += (n//i)
                    count += 2
                if count > 4:
                    return 0
            
            if count == 4:
                return total
            else:
                return 0

        d = Counter(nums)
        ans = 0
        for i in d:
            ans += getdivisors(i) * d[i]
        return ans