# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            if not node:
                return 0, 0
            
            lcoins, lsize = helper(node.left)
            rcoins, rsize = helper(node.right)

            total_size = lsize + rsize + 1
            total_coins = node.val + lcoins + rcoins
            self.ans += abs(total_coins - total_size)
            
            return total_coins, total_size
        
        self.ans = 0
        helper(root)
        return self.ans