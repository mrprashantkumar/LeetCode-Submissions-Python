class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        nums = [(i, j, k) for i, j , k in zip(indices, sources, targets)]
        nums.sort()

        ans = ""
        start = 0
        for i, j, k in nums:
            if start < i:
                ans += s[start:i]
                start = i
            l = len(j)
            if s[i:i+l] == j:
                ans += k
                start = i+l
            
        ans += s[start:]
        return ans