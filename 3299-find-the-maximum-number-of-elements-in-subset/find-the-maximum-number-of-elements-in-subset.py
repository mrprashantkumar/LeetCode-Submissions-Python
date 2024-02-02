class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        d = Counter(nums)

        ans = d[1] if d[1]&1 else d[1]-1
        for i in d:
            if i > 1:
                curr = 0
                power = 1
                while True:
                    if d[i**power] >= 2:
                        curr += 2
                        power *= 2
                    elif d[i**power] == 1:
                        curr += 1
                        break
                    else:
                        break
                curr = curr if curr&1 else curr-1
                ans = max(curr, ans)
        return ans