class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        ans=0
        for i in costs:
            if i<=coins:
                ans+=1
                coins-=i
            else:
                break
        return ans