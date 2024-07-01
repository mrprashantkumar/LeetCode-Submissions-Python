class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        n = len(arr)
        return any(arr[i]&1 == arr[i+1]&1 == arr[i+2]&1 == 1 for i in range(n - 2))