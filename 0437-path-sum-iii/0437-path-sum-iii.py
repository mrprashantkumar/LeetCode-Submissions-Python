# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def solve(root,Sum):
            nonlocal ans
            if root is None:
                return
            
            currsum=root.val+Sum
            x=currsum-targetSum
            if x in d:
                ans+=d[x]
            d[currsum] = d.get(currsum, 0) + 1
            solve(root.left,currsum)
            solve(root.right,currsum)
            d[currsum]-=1
        
        d={0:1}
        ans = 0
        solve(root,0)
        return ans