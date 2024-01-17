class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = Counter(arr)
        return len(set(d.keys()))==len(set(d.values()))