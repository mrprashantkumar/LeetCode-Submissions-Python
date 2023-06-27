class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        seen = []
        seen.append([s[0], 1])
        for ch in s[1:]:
            if seen and ch == seen[-1][0]:
                seen[-1][1] += 1
                if seen[-1][1] == k:
                    seen.pop()
            else:
                seen.append([ch, 1])

        return "".join(ch*count for ch, count in seen)