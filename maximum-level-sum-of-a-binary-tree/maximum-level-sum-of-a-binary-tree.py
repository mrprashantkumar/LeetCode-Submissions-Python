# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        qu = deque([root])
        ans = 1
        maxval = -1000000007
        level = 1
        while qu:
            n = len(qu)
            levelsum = 0
            for _ in range(n):
                curr = qu.popleft()
                levelsum += curr.val
                if curr.left:
                    qu.append(curr.left)
                if curr.right:
                    qu.append(curr.right)
            
            if levelsum>maxval:
                ans = level
                maxval = levelsum
            level += 1
        
        return ans