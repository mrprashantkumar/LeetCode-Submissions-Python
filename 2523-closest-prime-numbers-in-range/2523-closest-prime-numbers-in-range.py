class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        if left==right:
            return [-1, -1]
        
        prime = [True for i in range(right+1)]
        p = 2
        while (p*p <= right):
            if (prime[p] == True):
                for i in range(p * p, right+1, p):
                    prime[i] = False
            p+=1
        
        left = max(2, left)
        nums = [i for i in range(left, right+1) if prime[i] == True]
        n = len(nums)
        if n<2:
            return [-1, -1]
        
        diff = 10000007
        for i in range(n-1):
            if nums[i+1]-nums[i] < diff:
                ans = [nums[i], nums[i+1]]
                diff = nums[i+1]-nums[i]
        return ans