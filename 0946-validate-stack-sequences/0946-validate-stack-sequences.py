class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        seen = []
        n = len(pushed)
        i, j = 0, 0
        
        while i<n:
            seen.append(pushed[i])
            while seen and j<n and seen[-1] == popped[j]:
                seen.pop()
                j += 1
            i += 1
        return j==n