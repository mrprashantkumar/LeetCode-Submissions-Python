class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        ans = 0
        while mainTank >= 5 and additionalTank > 0:
            ans += 10*5
            mainTank -= 4
            additionalTank -= 1
        
        ans += 10*mainTank
        return ans