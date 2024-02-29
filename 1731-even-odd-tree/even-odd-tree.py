# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        nodes = deque()
        nodes.append(root)
        level = 0

        while nodes:
            curr = deque()
            for node in nodes:
                if node.val&1 == level&1:
                    return False
                
                if node.left:
                    if level&1:
                        if curr and curr[-1].val >= node.left.val:
                            return False
                    else:
                        if curr and curr[-1].val <= node.left.val:
                            return False
                    curr.append(node.left)
                
                if node.right:
                    if level&1:
                        if curr and curr[-1].val >= node.right.val:
                            return False
                    else:
                        if curr and curr[-1].val <= node.right.val:
                            return False
                    curr.append(node.right)

            nodes = curr
            level += 1
            
        return True