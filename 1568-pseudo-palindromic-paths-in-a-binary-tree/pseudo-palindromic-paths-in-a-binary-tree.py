# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def helper(node, pathsofar):
            if not node:
                return 0
            
            if not node.left and not node.right:
                pathsofar[node.val] += 1
                vals = pathsofar.values()
                oddcount = sum([i&1 for i in vals])
                pathsofar[node.val] -= 1
                if oddcount <= 1:
                    return 1
                else:
                    return 0
            
            pathsofar[node.val] += 1
            ans = helper(node.left, pathsofar) + helper(node.right, pathsofar)
            pathsofar[node.val] -= 1
            return ans
        
        return helper(root, defaultdict(int))