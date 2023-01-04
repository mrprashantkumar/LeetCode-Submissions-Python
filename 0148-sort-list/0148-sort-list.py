# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        li = []
        while head:
            li.append(head.val)
            head = head.next
        
        li.sort()
        
        x = None
        for i in li[::-1]:
            x = ListNode(i, x)
        return x