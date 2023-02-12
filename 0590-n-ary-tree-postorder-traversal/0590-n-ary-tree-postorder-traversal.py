"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def helper(root):
            if not root:
                return 
            nonlocal ans
            for child in root.children:
                helper(child)
            ans.append(root.val)
        ans = []
        helper(root)
        return ans