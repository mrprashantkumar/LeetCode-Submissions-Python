# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        def dfs(node):
            if not node:
                return [], 0
            
            if not node.left and not node.right:
                return [1], 0
            
            l_dists, l_count = dfs(node.left)
            r_dists, r_count = dfs(node.right)
            ans = 0
            for l in l_dists:
                for r in r_dists:
                    if l+r <= distance:
                        ans += 1

            l_dists = [i+1 for i in l_dists]
            r_dists = [i+1 for i in r_dists]

            return l_dists + r_dists, l_count + r_count + ans
        
        return dfs(root)[1]