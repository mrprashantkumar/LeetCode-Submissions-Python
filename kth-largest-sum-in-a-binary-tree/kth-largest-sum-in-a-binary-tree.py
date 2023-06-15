# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        vals = []
        qu = deque([root])
        while qu:
            l = len(qu)
            currLevel = 0
            for _ in range(l):
                curr = qu.popleft()
                currLevel += curr.val
                if curr.left:
                    qu.append(curr.left)
                if curr.right:
                    qu.append(curr.right)
            
            vals.append(currLevel)
        
        if k > len(vals):
            return -1
        vals.sort()
        return vals[-k]