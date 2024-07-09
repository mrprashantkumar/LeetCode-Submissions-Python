class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        n = len(customers)
        finish = 0
        totalWait = 0
        for i in range(n):
            finish = max(finish, customers[i][0])
            finish += customers[i][1]
            totalWait += finish - customers[i][0]
            
        return totalWait / n