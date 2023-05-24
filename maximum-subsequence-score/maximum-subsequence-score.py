class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n = len(nums1)
        pairs = [(i, j) for i, j in zip(nums1, nums2)]
        pairs.sort(key = lambda x : -x[1])

        kmax = [i for i, j in pairs[:k]]
        kmaxsum = sum(kmax)
        heapify(kmax)

        ans = kmaxsum * pairs[k-1][1]

        for i in range(k, n):
            kmaxsum -= heappop(kmax)
            kmaxsum += pairs[i][0]
            heappush(kmax, pairs[i][0])

            ans = max(ans, kmaxsum * pairs[i][1])
        return ans