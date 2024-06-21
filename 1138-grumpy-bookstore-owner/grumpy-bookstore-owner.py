class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        ans = 0
        for i in range(n):
            if grumpy[i] == 0:
                ans += customers[i]
        
        left = 0
        res = 0
        for right in range(n):
            if grumpy[right] == 1:
                    ans += customers[right]
            while (right-left) >= minutes:
                if grumpy[left] == 1:
                    ans -= customers[left]
                    res = max(res, ans)
                
                left += 1
            res = max(res, ans)
        return res