# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0, inf
            
            if not node.left and not node.right:
                return 0, node.val
            
            lans, lval = dfs(node.left)
            rans, rval = dfs(node.right)
            # print(node.val, lans, rans)

            if lval == node.val == rval:
                ans[0] = max(ans[0], 2+lans+rans)
                return 1+max(lans,rans), node.val
            elif lval == node.val:
                ans[0] = max(ans[0], 1+lans)
                return 1+lans, node.val
            elif rval == node.val:
                ans[0] = max(ans[0], 1+rans)
                return 1+rans, node.val
            else:
                return 0, node.val
        
        ans = [0]
        dfs(root)
        return ans[0]