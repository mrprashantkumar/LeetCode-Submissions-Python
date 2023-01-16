# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        def helper(root):
            if not root:
                return 
            helper(root.left)
            self.nums.append(root.val)
            self.n += 1
            helper(root.right)
        
        self.nums = []
        self.n = 0
        self.c = 0
        helper(root)

    def next(self) -> int:
        self.c += 1
        return self.nums[self.c -1]
        

    def hasNext(self) -> bool:
        if self.c < self.n:
            return True
        return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()