# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def helper(root, path, target):
            if not root:
                return 
            
            if not root.left and not root.right:
                if target == root.val:
                    ans.append(path+[root.val])
                    return 
            
            helper(root.left, path+[root.val], target-root.val)
            helper(root.right, path+[root.val], target-root.val)
        
        ans = []
        helper(root, [], targetSum)
        return ans