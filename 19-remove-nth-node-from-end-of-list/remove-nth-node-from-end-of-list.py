# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return 
        dummy = ListNode(-1, head)
        
        for _ in range(n):
            head = head.next
        
        if not head:
            return dummy.next.next
        
        curr = dummy.next
        while head.next:
            head = head.next
            curr = curr.next
        
        curr.next = curr.next.next
        return dummy.next