class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        def helper(currCity, fuelLeft):
            if fuelLeft < 0:
                return 0
                
            if dp[currCity][fuelLeft] != -1:
                return dp[currCity][fuelLeft]

            ans = 0
            if currCity == finish:
                ans = 1
            
            for city in range(n):
                if city != currCity:
                    ans += helper(city, fuelLeft - abs(locations[currCity] - locations[city]))
                    ans %= 1000000007
            
            dp[currCity][fuelLeft] = ans
            return ans
        
        n = len(locations)
        dp = [[-1]*(fuel+1) for _ in range(n)]
        return helper(start, fuel)