class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxi = max(candies)
        ans = []
        for candy in candies:
            if candy+extraCandies >= maxi:
                ans.append(True)
            else:
                ans.append(False)
        return ans