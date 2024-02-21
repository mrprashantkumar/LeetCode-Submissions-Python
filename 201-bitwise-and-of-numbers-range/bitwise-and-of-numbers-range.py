class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        arr1, arr2 = [0]*32, [0]*32
        for i in range(32):
            arr1[i] = left%2
            arr2[i] = right%2
            left //= 2
            right //= 2

        ans = 0
        for i in range(31, -1, -1):
            if arr1[i] == arr2[i]:
                ans += arr1[i] * 2**i
            else:
                break
        return ans