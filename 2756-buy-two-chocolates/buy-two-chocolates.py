class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        temp = money
        prices.sort()
        money -= prices[0]
        money -= prices[1]
        if money >= 0:
            return money
        return temp