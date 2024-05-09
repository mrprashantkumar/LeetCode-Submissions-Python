class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        ans = 0

        for i in range(k):
            curr = happiness.pop()
            ans += max(0, curr - i)
        
        return ans