class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        mini, secmini = math.inf, math.inf
        for i in nums:
            if i<mini:
                mini = i
            elif i<secmini and i != mini:
                secmini = i
            elif i>mini and i>secmini:
                return True
        return False