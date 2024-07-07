class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        emptyBottles = numBottles
        while numExchange <= emptyBottles:
            gained = emptyBottles // numExchange
            emptyBottles %= numExchange
            ans += gained
            emptyBottles += gained
        
        return ans

            