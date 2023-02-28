# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        def helper(root):
            if not root:
                return "#"
            
            left = helper(root.left)
            right = helper(root.right)
            string = str(root.val) +'('+left+')'+'('+right+')'
            
            if d[string] == 1:
                ans.append(root)
            d[string] += 1
            return string
        
        ans = []
        d = defaultdict(int)
        helper(root)
        return ans