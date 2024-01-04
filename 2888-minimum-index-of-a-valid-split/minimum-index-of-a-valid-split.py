class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        d = Counter(nums)
        n = len(nums)
        domele = -1
        for i in d:
            if d[i] * 2 > n:
                domele = i
                break
        
        count = [0]*n
        countsofar = 0
        for i in range(n):
            if nums[i] == domele:
                countsofar += 1
            count[i] = countsofar
        
        for i in range(n):
            if (count[i] * 2 > (i+1)) and ((countsofar - count[i]) * 2 > (n-i-1)):
                return i
        return -1