# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        def helper(node, val):
            if not node:
                return
            
            self.vals.add(val)
            helper(node.left, val*2 + 1)
            helper(node.right, val*2 + 2)
            return

        self.vals = set()
        helper(root, 0)

    def find(self, target: int) -> bool:
        return target in self.vals

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)