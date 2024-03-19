class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        maxi = max(milestones)
        tot = sum(milestones)
        rest = tot - maxi
        if maxi-1 <= rest:
            return tot
        return rest * 2 + 1