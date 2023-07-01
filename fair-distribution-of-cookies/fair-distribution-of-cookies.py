class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        def dfs(i, count):
            if n-i < count:
                return 1000000007
            
            if i == n:
                return max(nums)
            
            ans = 1000000007
            for j in range(k):
                count -= nums[j] == 0
                nums[j] += cookies[i]

                ans = min(ans, dfs(i+1, count))

                nums[j] -= cookies[i]
                count += nums[j] == 0
            
            return ans
        
        n = len(cookies)
        nums = [0]*k
        return dfs(0, k)