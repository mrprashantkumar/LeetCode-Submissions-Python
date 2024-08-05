class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d = Counter(arr)
        for i in d:
            if d[i] == 1:
                k -= 1
            if k == 0:
                return i
                
        return ""