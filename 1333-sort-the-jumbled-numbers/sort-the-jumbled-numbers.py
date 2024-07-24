class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        @cache
        def getMappedNum(n):
            ans = ''
            for d in str(n):
                ans += str(mapping[int(d)])
            return int(ans)
        
        pairs = []
        for i, x in enumerate(nums):
            pairs.append([getMappedNum(x), i])
        pairs.sort()
        return [nums[y] for x, y in pairs]