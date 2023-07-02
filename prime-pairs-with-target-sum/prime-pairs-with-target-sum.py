class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        def getPrimes(n):
            primes = [True]*(n+1)

            p = 2
            while p*p <= n:
                if primes[p]:
                    for k in range(p+p, n+1, p):
                        primes[k] = False
                p += 1
            
            res = []
            for i in range(2, n+1):
                if primes[i]:
                    res.append(i)
            return res

        nums = getPrimes(n)
        ans = []
        l = len(nums)
        i, j = 0, l-1
        while i<=j:
            ps = nums[i]+nums[j]
            if ps == n:
                ans.append([nums[i], nums[j]])
                i += 1
                j -= 1
            elif ps>n:
                j -= 1
            else:
                i += 1
        return ans