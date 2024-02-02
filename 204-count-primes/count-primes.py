class Solution:
    def countPrimes(self, n: int) -> int:
        primes = [True]*n

        p = 2
        while p*p < n:
            if primes[p]:
                i = 2*p
                while i < n:
                    primes[i] = False
                    i += p
            p += 1
        
        return sum(1 for i in primes[2:] if i)