# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        parent = defaultdict(None)
        mapping = {}
        allnodes = set()
        root = None
        for par, child, isLeft in descriptions:
            if par not in mapping:
                mapping[par] = TreeNode(par)
                allnodes.add(mapping[par])
            if child not in mapping:
                mapping[child] = TreeNode(child)
                allnodes.add(mapping[child])
            
            parent[mapping[child]] = mapping[par]
            if isLeft:
                mapping[par].left = mapping[child]
            else:
                mapping[par].right = mapping[child]
        
        for node in allnodes:
            if node not in parent:
                return node