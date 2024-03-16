class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        visited = set()
        pairs = [(x, i) for i, x in enumerate(nums)]
        heapify(pairs)
        tot = sum(nums)

        ans = []
        for idx, k in queries:
            if idx not in visited:
                tot -= nums[idx]
                visited.add(idx)
            
            while k and pairs:
                val, ind = heappop(pairs)
                if ind not in visited:
                    tot -= val
                    visited.add(ind)
                    k -= 1
            
            ans.append(tot)
        return ans