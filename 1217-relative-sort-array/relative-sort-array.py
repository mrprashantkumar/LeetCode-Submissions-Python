class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d = {x:i for (i, x) in enumerate(arr2)}
        return sorted(arr1, key = lambda x : (d.get(x, inf), x))