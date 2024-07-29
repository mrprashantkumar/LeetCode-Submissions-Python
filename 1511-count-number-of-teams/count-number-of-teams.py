class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)

        ans = 0
        for i in range(1, n-1):
            leftmini, rightmini = 0, 0
            leftmaxi, rightmaxi = 0, 0

            for j in range(i):
                if rating[j] < rating[i]:
                    leftmini += 1
                elif rating[j] > rating[i]:
                    leftmaxi += 1
            
            for j in range(i+1, n):
                if rating[i] < rating[j]:
                    rightmaxi += 1
                elif rating[i] > rating[j]:
                    rightmini += 1
            
            ans += leftmini * rightmaxi
            ans += leftmaxi * rightmini
        
        return ans