class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = 0
        pref = 0
        for i in gain:
            pref += i
            ans = max(ans, pref)
        return ans