class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        qu = deque()
        for i in range(k):
            while qu and nums[i] >= nums[qu[-1]]:
                qu.pop()
            qu.append(i)
        
        ans = []
        ans.append(nums[qu[0]])

        for i in range(k, n):
            if qu and qu[0] == i-k:
                qu.popleft()
            
            while qu and nums[i] >= nums[qu[-1]]:
                qu.pop()
            qu.append(i)

            ans.append(nums[qu[0]])
        
        return ans