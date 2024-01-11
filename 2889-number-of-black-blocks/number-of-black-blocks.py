class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        d = defaultdict(int)

        for x, y in coordinates:
            for dx in range(2):
                for dy in range(2):
                    a, b = x-dx, y-dy
                    if 0 <= a < m-1 and 0 <= b < n-1:
                        key = a*n + b
                        d[key] += 1
                        
        ans = [0] * 5
        for val in d.values():
            ans[val] += 1
        ans[0] = (n-1) * (m-1) - len(d.values())
        return ans