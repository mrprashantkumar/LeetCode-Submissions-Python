class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        ans = 0
        seen = Counter()
        left, right = 0, 0
        
        while right <n:
            seen[fruits[right]] += 1
            right += 1
            
            while len(seen) >= 3:
                seen[fruits[left]] -= 1
                if seen[fruits[left]] == 0:
                    del seen[fruits[left]]
                left += 1
            
            ans = max(ans, right-left)
        return ans