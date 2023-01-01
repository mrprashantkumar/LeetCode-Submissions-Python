class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        s = set()
        for i in nums:
            r = int(math.sqrt(i))
            
            for j in range(2, r+1):
                if i%j==0:
                    s.add(j)
                    while i%j==0:
                        i//=j
            if i>1:
                s.add(i)
        
        return len(s)