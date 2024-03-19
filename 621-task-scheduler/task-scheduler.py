class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = Counter(tasks)
        maxi = max(d.values())
        maxCount = sum(1 for i in d if d[i] == maxi)
        return max(len(tasks), (maxi - 1) * (n+1) + maxCount)