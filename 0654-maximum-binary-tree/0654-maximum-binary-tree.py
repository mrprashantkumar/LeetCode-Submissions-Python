# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(arr, start, end):
            if start>end:
                return None
            
            maxind = start
            maxval = arr[start]
            for i in range(start, end+1):
                if arr[i]>maxval:
                    maxval = arr[i]
                    maxind = i
            
            root = TreeNode(arr[maxind])
            root.left = helper(arr, start, maxind-1)
            root.right = helper(arr, maxind+1, end)
            
            return root
        
        return helper(nums, 0, len(nums)-1)