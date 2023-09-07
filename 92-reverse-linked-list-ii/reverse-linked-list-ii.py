# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head.next or left == right:
            return head
        
        dummy = ListNode(-1, head)

        curr = dummy
        for _ in range(right):
            curr = curr.next
        
        rightNode = curr
        rightNext = curr.next
        rightNode.next = None

        curr = dummy
        for _ in range(left-1):
            curr = curr.next

        leftPrev = curr
        leftNode = curr.next
        leftPrev.next = None

        curr = leftNode
        prev = None

        while curr:
            nextt = curr.next
            curr.next = prev
            prev = curr
            curr = nextt

        leftPrev.next = prev
        leftNode.next = rightNext

        return dummy.next