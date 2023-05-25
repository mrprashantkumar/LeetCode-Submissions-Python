# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        def helper(root):
            if not root:
                return -1
            
            if not root.left and not root.right:
                ans[0].append(root.val)
                return 0
            
            lh = helper(root.left)
            rh = helper(root.right)
            
            ind = max(lh, rh)+1
            if ind >= len(ans):
                ans.append([])
            ans[ind].append(root.val)
            return ind
        
        ans = [[]]
        helper(root)
        return ans