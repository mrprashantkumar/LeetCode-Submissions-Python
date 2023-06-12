class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        n = len(nums)
        seen = []
        for i in nums:
            if not seen:
                seen.append(i)
                start = i
                end = i
            elif seen[-1]+1 == i:
                seen.append(i)
                end = i
            else:
                if start == end:
                    ans.append(str(start))
                else:
                    ans.append(str(start)+"->"+str(end))
                seen = [i]
                start = i
                end = i
        if seen:
            if start == end:
                    ans.append(str(start))
            else:
                ans.append(str(start)+"->"+str(end))
        return ans