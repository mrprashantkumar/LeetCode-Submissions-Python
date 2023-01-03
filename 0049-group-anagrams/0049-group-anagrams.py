class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=defaultdict(list)
        for w in strs:
            d[tuple(sorted(w))].append(w)
        return d.values()