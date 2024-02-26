# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        @cache
        def dfs(node):
            if not node:
                return 0
            
            lsum = dfs(node.left)
            rsum = dfs(node.right)

            return node.val + lsum + rsum

        def check(node):
            if not node:
                return True, -inf, inf
            
            isvalidl, lmin, lmax = check(node.left)
            isvalidr, rmin, rmax = check(node.right)
            # print(node.val, isvalidl, lmin, lmax, isvalidr, rmin, rmax)

            if isvalidl and isvalidr and lmin < node.val < rmax:
                BSTnodes.append(node)
            else:
                return False, -inf, inf
            
            return True, max(node.val, lmin, rmin), min(node.val, rmax, lmax)
        
        BSTnodes = []
        check(root)

        ans = 0
        for node in BSTnodes:
            ans = max(ans, dfs(node))
        return ans