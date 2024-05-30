class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        pref = [0]
        for i in arr:
            pref.append(i ^ pref[-1])
        
        ans = 0

        for i in range(n):
            curr1 = arr[i]
            for j in range(i+1, n):
                curr1 ^= arr[j]
                curr2 = arr[j]
                for k in range(j, n):
                    curr2 ^= arr[k]
                    if curr1 == curr2:
                        ans += 1
                
        return ans