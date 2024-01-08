class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        s = set(nums)
        for i, j in zip(moveFrom, moveTo):
            s.remove(i)
            s.add(j)
        return sorted(list(s))