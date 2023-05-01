class Solution:
    def average(self, salary: List[int]) -> float:
        n = len(salary)
        mini, maxi = 100000007, 0
        total = 0
        for i in salary:
            mini = min(mini, i)
            maxi = max(maxi, i)
            total += i
        
        return (total-mini-maxi)/(n-2)