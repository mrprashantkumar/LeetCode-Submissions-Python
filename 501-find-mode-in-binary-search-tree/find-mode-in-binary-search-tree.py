# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def helper(node):
            if not node:
                return 
            
            count[node.val] += 1
            self.maxval = max(self.maxval, count[node.val])
            helper(node.left)
            helper(node.right)
            return
        
        count = Counter()
        self.maxval = 0
        helper(root)
        ans = []
        for node in count:
            if count[node] == self.maxval:
                ans.append(node)
        return ans