"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        graph = defaultdict(list)
        for node in tree:
            for child in node.children:
                graph[child.val].append(node.val)
                
        for node in tree:
            if len(graph[node.val]) == 0:
                return node