class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ages.sort()
        n = len(ages)
        ans = 0
        i = 0
        while i < n:
            val, count = ages[i], 0
            while i < n and ages[i] == val:
                i += 1
                count += 1
            idx = bisect_right(ages, ages[i-1]/2 + 7)
            ans += max(0, (i - idx - 1)*count)

        return ans