# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr and curr.next:
            curr = curr.next
            while curr and curr.next and curr.next.val != 0:
                curr.val += curr.next.val
                curr.next = curr.next.next
            curr = curr.next
        
        head = head.next
        curr = head
        while curr and curr.next and curr.next.next:
            curr.next = curr.next.next
            curr = curr.next
        curr.next = None
        return head