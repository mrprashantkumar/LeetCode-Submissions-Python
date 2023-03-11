# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def helper(start, end):
            if start>end:
                return None
            
            mid = (start+end)//2
            root = TreeNode(nums[mid])
            root.left = helper(start, mid-1)
            root.right = helper(mid+1, end)
            
            return root
        
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        
        return helper(0, len(nums)-1)