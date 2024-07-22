class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        pairs = [(i, j) for i, j in zip(names, heights)]
        pairs.sort(key = lambda x : -x[1])
        return [i for i, _ in pairs]