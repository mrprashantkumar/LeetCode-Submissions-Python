class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n % k != 0:
            return False
        
        d = Counter(nums)
        for _ in range(n // k):
            mini = min(d)
            for i in range(k):
                if d[mini] > 0:
                    d[mini] -= 1
                    if d[mini] == 0:
                        del d[mini]
                    mini += 1
                else:
                    return False
        
        return True