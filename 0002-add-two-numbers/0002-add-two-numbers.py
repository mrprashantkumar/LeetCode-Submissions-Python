# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        carry=0
        dummy = ListNode(-1)
        head = dummy
        while curr1 or curr2 or carry:
            dsum = 0
            dsum += carry
            carry = 0
            if curr1:
                dsum += curr1.val
                curr1 = curr1.next
            if curr2:
                dsum += curr2.val
                curr2 = curr2.next
            carry = dsum//10
            head.next = ListNode(dsum%10)
            head = head.next
        return dummy.next