# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        def dfs(node):
            if not node:
                return
            
            node.left = dfs(node.left)
            node.right = dfs(node.right)

            if node.val in to_delete:
                if node.left:
                    self.ans.append(node.left)
                if node.right:
                    self.ans.append(node.right)
                return None
                
            return node

        to_delete = set(to_delete)
        self.ans = []
        root = dfs(root)
        if root:
            self.ans.append(root)
        return self.ans